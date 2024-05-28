"""
Combine aliased colors
"""

import json

with open("../data/processed_colors.json","r") as fp:
    colors = json.load(fp)

combined_colors = dict()
def find_master_id(id):
    if id in combined_colors:
        return id
    for master_id,color in combined_colors.items():
        if id in color["ids"]:
            return master_id
    return None

def new_master_color(color):
    return {
        "ids": [color["id"], *color["aliases"]],
        "names": [color["name"]],
        "hex": color["hex"],
        "description": color["description"],
        "url": color["url"],
        "lrv": color["lrv"],
        "best_selling": color["best_selling"],
        "available": color["available"],
        "exterior": color["exterior"],
        "families": [color["family"]],
        "stains": list(color["stains"].keys()),
        "images": [color["image"]] if color["image"] else [],
        "matching": color["matching"],
        "similar": color["similar"],
        "shades": color["shades"],
        "palettes": color["palettes"],
        "tags": color["tags"]
    }

def combine_color_into_master(color, master):
    # Check that they are, in fact, the same color
    if master["hex"] != color["hex"]:
        print(f"{master['ids']} and {color['id']}: different hex values ({master['hex']} and {color['hex']})")

    # Append lists with unique values
    for id in [color["id"], *color["aliases"]]:
        if id not in master["ids"]:
            master["ids"].append(id)

    for name in [color["name"]]:
        if name not in master["names"]:
            master["names"].append(name)

    if color["family"] not in master["families"]:
            master["families"].append(color["family"])

    for stain in color["stains"].keys():
        if stain not in master["stains"]:
            master["stains"].append(stain)

    if color["image"]:
        if all(image["alt_text"][:15] != color["image"]["alt_text"][:15] for image in master["images"]):
            master["images"].append(color["image"])

    for match in color["matching"]:
        if match not in master["matching"]:
            master["matching"].append(match)

    for id in color["similar"]:
        if id not in master["similar"]:
            master["similar"].append(id)

    for id in color["shades"]:
        if id not in master["shades"]:
            master["shades"].append(id)

    for palette in color["palettes"]:
        if palette not in master["palettes"]:
            master["palettes"].append(palette)

    for tag in color["tags"]:
        if tag not in master["tags"]:
            master["tags"].append(tag)

    # Overwrite values
    if master["description"].startswith("Also known as"):
        master["description"] = color["description"]
        master["url"] = color["url"]
        master["lrv"] = color["lrv"]

    master["best_selling"] = master["best_selling"] or color["best_selling"]
    
    master["available"] = master["available"] or color["available"]
    
    if color["exterior"] == "available":
        master["exterior"] = "available"
    if color["exterior"] == "not recommended" and master["exterior"] != "available":
        master["exterior"] == "not recommended"
    
    return master_color

print("Combining colors")
for id,color in colors.items():
    master_id = find_master_id(id)
    
    if master_id is None:
        combined_colors[id] = new_master_color(color)
    else:
        master_color = combined_colors[master_id]
        combined_colors[master_id] = combine_color_into_master(color, master_color)


"""
print("Resolving matching ids")
for id in combined_colors:
    for m in range(len(combined_colors[id]["matching"])):
        for i in range(len(combined_colors[id]["matching"][m])):
            matchid = combined_colors[id]["matching"][m][i]
            combined_colors[id]["matching"][m][i] = find_master_id(matchid)
    
print("Resolving similar ids")
for id in combined_colors:
    for s in range(len(combined_colors[id]["similar"])):
        similarid = combined_colors[id]["similar"][s]
        combined_colors[id]["similar"][s] = find_master_id(similarid)
    combined_colors[id]["similar"] = list(set(combined_colors[id]["similar"]))

print("Resolving shade ids")
for id in combined_colors:
    for s in range(len(combined_colors[id]["shades"])):
        similarid = combined_colors[id]["shades"][s]
        combined_colors[id]["shades"][s] = find_master_id(similarid)
    combined_colors[id]["shades"] = list(set(combined_colors[id]["shades"]))
"""

for idA,colorA in combined_colors.items():
    for idB,colorB in combined_colors.items():
        if idB != idA and colorA["hex"] == colorB["hex"]:
            print(f"{idA} and {idB} might be the same color (hex values are the same)")

print("Writing to combined_colors.json")
with open("../data/combined_colors.json", "w") as fs:
    json.dump(combined_colors, fs, indent=4)

