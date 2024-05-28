"""
Pre-process color data into an easier-to-use format
"""

import json

with open("../data/colors.json","r") as fp:
    colors = json.load(fp)

processed_colors = dict()
for color in colors:
    id = color["number"]
    processed_color = {
        "id": id,
        "name": color["name"],
        "hex": "#"+color["hex"],
        "description": color["description"],
        "family": color["family"],
        "url": color["url"],
        "lrv": color["lrv"],
        "best_selling": color["is_best_selling"],
        "available": color["estore_available"],
        "exterior": color["exterior_availability"],
        "stains": {},
        "image": color["hero_image"] if color["hero_image"]["medium"] else None,
        "aliases": [],
        "matching": [],
        "similar": [similar["number"] for similar in color["similar"]],
        "shades": [shade["number"] for shade in color["shades"]],
        "palettes": [palette["name"] for palette in color["palettes"]],
        "tags": [tag_value for tag_type in color["tags"] for tag_value in tag_type["value"]]
    }

    for stain in color["stain_opacities"]:
        name = stain["opacity"]
        r = stain.get("r", color["r"])
        g = stain.get("g", color["g"])
        b = stain.get("b", color["b"])
        processed_color["stains"][name] = f"#{r:X}{g:X}{b:X}"

    aliases = []
    if color["aliases"]:
        aliases = color["aliases"].split(", ")
    for eq in color["equivalent"]:
        aliases.append(eq["number"])
    for i in range(len(aliases)):
        alias = aliases[i]
        while len(alias) <= 2:
            alias = "0"+alias
        aliases[i] = alias
    processed_color["aliases"] = list(set(aliases))

    for group in color["harmony"]:
        for harmony in group:
            matching = []
            for harmonic in harmony:
                matching.append(harmonic["number"])
            matching.sort()
            processed_color["matching"].append(matching)

    processed_colors[id] = processed_color

print("Writing to processed_colors.json")
with open("../data/processed_colors.json", "w") as fs:
    json.dump(processed_colors, fs, indent=4)


