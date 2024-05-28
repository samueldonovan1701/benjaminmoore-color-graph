import "https://cdnjs.cloudflare.com/ajax/libs/vivagraphjs/0.12.0/vivagraph.min.js"

class Node {
    constructor(graph, id, data={}) {
        data.id = id;
        data.graph = graph;

        if(!graph.hasNode(id)) {
            data.is_expanded = false;
        } else {
            let node = graph.getNode(id);
            if(node.data === undefined || node.data.is_expanded === undefined) {
                data.is_expanded = false;
            }
            else {
                data.is_expanded = node.data.is_expanded;
            }
        }
        // Combine Viva Graph into this object
        for(let n in data) {
            this[n] = data[n];
        }

        return graph.addNode(id, this);
    }
    render(ele) {
        let g = Viva.Graph.svg("g", {id:this.id});

        g.appendChild(ele);

        g.addEventListener('click', (e) => this.on_click(e))
        g.addEventListener('dblclick', (e) => this.on_double_click(e))
        return g;
    }
    expand() {
        this.is_expanded = true;
    }
    collapse() {
        this.is_expanded = false;
        let nodes_to_remove = [];
        this.graph.forEachLinkedNode(this.id, (neighbor,link) => {
            if(link.fromId === this.id) {
                if(neighbor.links.length == 1)
                    nodes_to_remove.push(neighbor.id);
            }
        });
        nodes_to_remove.forEach((id) => this.graph.removeNode(id));
        return nodes_to_remove;
    }
    on_click(e) {
        this.graph.beginUpdate();
        if(this.is_expanded) {
            this.collapse();
        }
        else {
            this.expand();
        }
        this.graph.endUpdate();
    }
    on_double_click(e) {
        this.collapse();
        let links_to_remove = [];
        this.graph.forEachLinkedNode(this.id, (neighbor,link) => {
            if(link.fromId === this.id) {
                links_to_remove.push(link);
            }
        });
        links_to_remove.forEach((id) => this.graph.removeLink(id));
        return links_to_remove;
    }
    on_right_click(e) {

    }
}
export class ColorNode extends Node {
    constructor(graph, id) {
        return super(graph, id, graph.getColorData(id));
    }
    render() {
        let g = Viva.Graph.svg("g");
        if(this.lrv < 35) {
            g.attr("class", "colornode dark");
        }
        else {
            g.attr("class", "colornode light");
        }

        // Shape
        let shape = g.append("circle");
        
        // Size
        let size = 40;
        shape.attr("r", size);

        // Color
        shape.attr("fill", this.hex);

        // Label
        let label = Viva.Graph.svg("text", {
            id: `${this.id}_label`,
            x: 0,
            y: 0,
            "text-anchor": "middle",
            "dominant-baseline": "middle"
        });
        label.innerHTML = this.id;
        g.appendChild(label);
        
        return super.render(g);
    }
    expand(branch_name="") {
        let r = [];
        for(let branch in this.branches) {
            if(branch.includes(branch_name)) {
                r.push(new BranchNode(this.graph, this.id, branch));
            }
        }
        super.expand();
        return r;
    }
}
export class BranchNode extends Node {
    constructor(graph, color_id, branch_name) {
        let color = graph.getColorData(color_id);
        if(!color.branches.hasOwnProperty(branch_name)) {
            throw `No such branch ${branch_name} in ${color_id}`;
        }
        let colors = color.branches[branch_name];

        

        let id = `${color_id}_${branch_name}`;
        // Link first if possible to get neighborhood placement
        if(graph.hasNode(color_id)) {
            graph.addLink(color_id, id);
        }
        return super(graph, id, {name: branch_name, colors: colors});
    }

    render() {
        let g = Viva.Graph.svg("g");

        // Shape
        let shape = g.append("circle");
        shape.attr("class", "branchnode");
        
        // Size
        shape.attr("r", 25);

        // Color
        if(this.colors.length == 0) {
            throw `${this.id} has no colors`;
        }
        else if(this.colors.length == 1) {
            shape.attr("fill", this.graph.getColorData(this.colors[0]).hex);
        }
        else {
            //Linear gradient
            let fillgradient_id = this.id+"_fillgradient"
            let fillgradient = Viva.Graph.svg("linearGradient", {id: fillgradient_id});

            let offset_step = 100 / (this.colors.length+1);
            this.colors.forEach((color_id,i) => {
                fillgradient.append("stop")
                            .attr("offset", (offset_step*(i+1))+"%")
                            .attr("stop-color", this.graph.getColorData(color_id).hex);
            });
            
            shape.attr("fill", `url(#${fillgradient_id})`)
            g.appendChild(fillgradient);
        }

        // Label
        let label = Viva.Graph.svg("text", {
            id: `${this.id}_label`,
            x: 0,
            y: 0,
            "text-anchor": "middle",
            "dominant-baseline": "middle"
        });
        label.innerHTML = this.name;
        g.appendChild(label);
        
        return super.render(g);
    }

    expand(add_nodes=true) {
        let r = [];
        this.colors.forEach((color_id) => {
            if(!add_nodes) {
                let node = this.graph.getNode(color_id);
                if(node === undefined) {
                    return;
                }
                else if(node.links.length > 2) {
                    return;
                }
                else {
                    this.graph.addLink(this.id, color_id);
                    super.expand();
                }
            }
            else {
                this.graph.addLink(this.id, color_id);
                r.push(new ColorNode(this.graph, color_id));
                super.expand();
            }
        });
        return r;
    }
}

export class ColorGraph{
    #graph;
    // Create
    constructor(containerID, colors, groups) {
        /*  colors = {
                "id": {
                    "alt_ids": ["idA", "idB", ...],
                    "names": ["Black", "Charcoal", ...],
                    "hex": "#000000",
                    "description": "lorem ipsum",
                    "url": "https://www.example.com",
                    "images": [
                        { 
                            "url":"https://www.example.com/image.jpg",
                            "alt_text": "An image"
                        },
                        ...
                    ]
                    "branches": {
                        "branch_name": ["colorA", "colorB", ...],
                        ...
                    },
                    "r_branches": {
                        "color_id": ["branch_name", ...]
                    }
                    ....
                }
            }
            groups = {
                "category": {
                    "id" {
                        "url": "http://www.example.com",
                        "description": "lorem ipsum",
                        "colors": ["colorA", "colorB", ...]
                    },...
                },...
            }
        */

        // Store colors/groups
        this.colors = colors;
        this.groups = groups;

        // Setup Viva Graph
        let container = document.getElementById(containerID);
        this.#graph = Viva.Graph.graph();
        
        // Define how things are displayed
        let graphics = Viva.Graph.View.svgGraphics();
        this.svg = graphics.getSvgRoot();
        this.svg.attr("class", "color-graph");

        let defs = this.svg.append("defs");

        let marker = Viva.Graph.svg("marker", { // https://github.com/anvaka/VivaGraphJS/blob/master/demos/tutorial_svg/05%20-%20Edges%20With%20Arrows.html
            id: "arrow",
            viewBox: "0 0 10 10",
            refX: "10",
            refY: "5",
            markerUnits: "strokeWidth",
            markerWidth: "10",
            markerHeight: "5",
            orient: "auto"
        });
        marker.append("polyline").attr('points', "0,0 10,5 0,10");
        
        defs.append(marker);
        
        
        graphics.node((node) => node.data ? node.data.render() : Viva.Graph.svg("g", {id:node.id}));

        graphics.placeNode((nodeUI, pos) => nodeUI.attr('transform', `translate(${pos.x}, ${pos.y})`));

        graphics.link((link) => {
            return Viva.Graph.svg("path", {stroke: "#000", "marker-mid":"url(#arrow)"});
        });

        graphics.placeLink((linkUI, posA, posB) => {
            let mid = {x: (posA.x+posB.x)/2, y: (posA.y+posB.y)/2}
            linkUI.attr("d", `M ${posA.x} ${posA.y} L ${mid.x} ${mid.y} L ${posB.x} ${posB.y}`)
        });

        // Run display
        let renderer = Viva.Graph.View.renderer(this.#graph, {
            graphics: graphics,
            container: container
        });
        renderer.run();

        // Combine Viva Graph into this object
        let prototype = Object.getPrototypeOf(this);
        for(let n in {...this.#graph}) {
            if(!prototype.hasOwnProperty(n))
                this[n] = this.#graph[n];
        }

        return this;
    }

    addLink(nodeA, nodeB) {
        if(!this.#graph.hasLink(nodeA, nodeB)) {
            this.#graph.addLink(nodeA, nodeB);
        }
    }

    
    
    getColorData(id) {
        if(!this.colors.hasOwnProperty(id)) {
            throw `No such color ${id}`;
        }
        else {
            return this.colors[id];
        }
    }
    showColor(color) {
        return new ColorNode(this, color);
    }
    showColorSolo(color) {
        this.#graph.beginUpdate();
        this.#graph.clear();

        color = new ColorNode(this, color);

        Object.entries(color.data.r_branches).forEach(([k,v]) => {
            v.forEach(branch_name => {
                if(branch_name !== "similar" && branch_name !== "shades") {
                    let other = new ColorNode(this, k);
                    let branch = other.data.expand(branch_name)[0];
                    branch.data.expand();
                    other.data.is_collapsed = false;
                }
            });
        });
        
        this.#graph.endUpdate();
    }

    getGroup(id) {
        for(let category in this.groups) {
            for(let group in this.groups[category]) {
                if(group === id) {
                    return this.groups[category][id];
                }
            }
        }
        throw `No such group ${id}`;
    }
    showGroup(name, ...expand) {
        this.#graph.beginUpdate();
        this.#graph.clear();

        let group = this.getGroup(name);
        group.colors.forEach(color => {
            let node = this.getNode(color);
            if(!node) {
                node = new ColorNode(this, color);
            }

            expand.forEach(branch_name => {
                let branch = node.data.expand(branch_name)[0];
                if(branch !== undefined) {
                    branch.data.expand(false);
                }
            });
        });
        
        this.#graph.endUpdate();
    }
};