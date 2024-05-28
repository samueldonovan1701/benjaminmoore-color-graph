"""
Truncate colors to only the necesarry fields and turn one-way references into two-way
"""

import json

with open("../data/combined_colors.json","r") as fp:
    colors = json.load(fp)

def resolve_links(color):
    def find_master_id(id):
        for master_id in colors:
            if id in colors[master_id]["ids"]:
                return master_id
        return None 

    for m,match in enumerate(color["matching"]):
        for i,id in enumerate(match):
            color["matching"][m][i] = find_master_id(id)
    for i,id in enumerate(color["similar"]):
        color["similar"][i] = find_master_id(id)
    for i,id in enumerate(color["shades"]):
        color["shades"][i] = find_master_id(id)
        
    return color

final_colors = dict()
for id,color in colors.items():
    color = color.copy()
    color = resolve_links(color)

    color["branches"] = {}

    if(len(color["shades"]) > 0):
        color["branches"]["shades"] = color["shades"]

    if(len(color["similar"]) > 0):
        color["branches"]["similar"] = color["similar"]
    
    for m,match in enumerate(color["matching"]):
        if(len(match) > 0):
            color["branches"][chr(65+m)] = match

    del color["exterior"]
    del color["stains"]
    del color["families"]
    del color["palettes"]
    del color["tags"]
    del color["matching"]
    del color["similar"]
    del color["shades"]

    final_colors[id] = color

print("Finding reverse links....")
for id, color in final_colors.items():
    color["r_branches"] = {}
    for other_id, other in final_colors.items():
        for branch_name, branch in other["branches"].items():
            if id in branch:
                if other_id not in color["r_branches"]:
                    color["r_branches"][other_id] = []
                color["r_branches"][other_id].append(branch_name)


print("Writing to final_colors.json")
with open("../data/final_colors.json", "w") as fs:
    json.dump(final_colors, fs, indent=4)

print("Writing to final_colors.min.json")
with open("../data/final_colors.min.json", "w") as fs:
    json.dump(final_colors, fs, separators=(',', ':'))
