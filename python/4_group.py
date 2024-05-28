import json

with open("../data/combined_colors.json","r") as fp:
    colors = json.load(fp)

aliases = {
    "Benjamin Moore Classics&reg;": "Benjamin Moore Classics®",
    "Color Preview&reg;": "Color Preview®",
    "Affinity&reg; Color Collection": "Affinity®",
    "Historical Colors": "Historical",
    "Off White Collection": "Off White",
    "Color Stories&reg;": "Color Stories®",
    "Williamsburg&reg; Paint Color Collection": "Williamsburg®",
    "Williamsburg Color Collection": "Williamsburg®",
    "Arborcoat Stain Colors": "Arborcoat",
    "Colors for Vinyl ": "Colors for Vinyl",
    "Color Trends 2024": "2024",
    "Color Trends 2023": "2023",
    "Color Trends 2022": "2022",
    "Color Trends 2021": "2021",
    "Color Trends 2020": "2020",
    "Color Trends 2019": "2019",
    "Color Trends 2018": "2018",
    "Color Trends 2017": "2017",
    "Color Trends 2016": "2016",
    "Color Trends 2015": "2015",
    "Color Trends 2014": "2014",
    "Beige": "Neutral",
    "Cream": "Neutral",
    "Peach": "Pink",
    "N/A": "None",
    "ultraflatsolid": "Ultra Flat Solid",
    "solid": "Solid",
    "semisolid": "Semi-Solid",
    "semitransparent": "Semi-Transparent",
    "translucent": "Translucent",
    

    "Woodluxe<sup><small>&reg;</small></sup> Exterior Wood Stain Colors": "Wood Stain",
    "Ready-Mix Color": "Ready Mix Colors",
}
groups = {
    "Special": {
        "Best Selling" : {
            "name": "Best Selling",
            "url": "https://www.benjaminmoore.com/en-us/color-overview/color-palettes/best-selling-colors",
            "description": "Explore Benjamin Moore's best-selling, most beloved paint colors"
        },
        "Available Online": {
            "name": "Available Online",
            "url": "https://www.benjaminmoore.com",
            "description": "Avialable for purchase online at www.benjaminmoore.com"
        },
    },
    "Collections": {
        "Benjamin Moore Classics®": {
            "url": "https://www.benjaminmoore.com/en-us/color-overview/color-palettes/classics-collection",
            "description": "A collection of 1,680 reliable and timeless hues."
        },
        "Color Preview®": {
            "url": "https://www.benjaminmoore.com/en-us/paint-colors/color-preview",
            "description": "A balanced collection that provides gradations of color mathematically arranged by hue and value, with vibrant shades and subtle hues."
        },
        "Affinity®": {
            "url": "https://www.benjaminmoore.com/en-us/paint-colors/affinity-color-collection",
            "description": "A meticulously curated collection with colors deisgned to complement one another, no matter which are chosen."
        },
        "Historical": {
            "url": "https://www.benjaminmoore.com/en-us/paint-colors/historical-collection",
            "description": "Comprised of time-honored colors inspired by American history and its rich architectural tradition."
        },
        "Off White": {
            "url": "https://www.benjaminmoore.com/en-us/paint-colors/off-white-collection",
            "description": "The ultimate collection of white and off-white paint colors gleaned from Benjamin Moore's long history and compiled from several collections."
        },
        "Color Stories®": {
            "url": "https://www.benjaminmoore.com/en-us/paint-colors/color-stories",
            "description": "A series of striking hues crafted to take on different appearances as the light changes."
        },
        "Designer Classics": {
            "url": "https://www.benjaminmoore.com/en-us/paint-colors/designer-classics",
            "description": "an elegant selection of hues made up of popular colors from different collections and a handful of unique hues."
        },
        "Williamsburg®": {
            "url": "https://www.benjaminmoore.com/en-us/paint-colors/williamsburg-paint-color-collection",
            "description": "A diverse collection of historic colors rooted in the artifacts and homes of Colonial Williamsburg, seen through a contemporary lens."
        },
        "Arborcoat": {
            "url": "https://www.benjaminmoorecoatings.com/collections/arborcoat-stain-colors-paint-colors",
            "description": "Discover Benjamin Moore's curated palette of 75+ stain colors for decks, siding, and trim."
        },
        "America's Colors": {
            "url": "https://www.benjaminmoore.com/en-us/3500-colors",
            "description": "Coastlines, grasslands, mountains, cities and suburbs—the diverse geography of the U.S. offers endless inspiration."
        },
        "Colors for Vinyl" : {
            "url": "https://www.benjaminmoore.com/en-us/project-ideas-inspiration/exteriors/vinyl-siding-ideas-inspiration",
            "description": "Refresh your vinyl with these popular Benjamin Moore colors.",
        },
        "Candice Olson Colors": {
            "url": "",
            "description": ""
        }
    },
    "Color Trends": {
        "2024" : {
            "url": "https://www.benjaminmoore.com/en-us/paint-colors/color-of-the-year-2024",
            "description": "New horizons are sought by exploring disparate places, thoughts, and colors to form endless creative possibilities. Softly saturated with a nuanced approach to contrast, the Benjamin Moore Color Trends 2024 palette takes inspiration from the hues experienced through travels and moments that span beyond routine."
        },
        "2023" : {
            "url": "https://www.benjaminmoore.com/en-us/paint-colors/color-of-the-year-2023",
            "description": "Each of these eight confident hues offer inspiration and creativity, while encouraging a push beyond the traditional to experience truly exceptional color."
        },
        "2022" : {
            "url": "https://www.benjaminmoore.com/en-us/color-overview/color-palettes/color-of-the-year-2022",
            "description": "The Color Trends 2022 palette of 14 hues, which includes October Mist, is harmonious yet diverse, reliable yet whimsical, and meditative yet eclectic. With its endless number of invigorating combinations, this palette provides effortless harmony for any paint project, and every design style."
        },
        "2021" : {
            "url": "https://www.benjaminmoore.com/en-us/color-overview/color-palettes/color-of-the-year-2021",
            "description": "Nourish the spirit with the comforting, sunbaked hues of the Color Trends 2021 palette, including Aegean Teal 2136-40."
        },
        "2020" : {
            "url": "https://www.benjaminmoore.com/en-us/color-overview/color-palettes/color-of-the-year-trends-2020",
            "description": "The ten harmonious hues of the Color Trends 2020 delivers modern paint color pairings that combine optimism with understatement, a timeless way to lighten up."
        },
        "2019" : {
            "url": "https://www.benjaminmoore.com/en-us/color-overview/color-palettes/color-trends-2019",
            "description": "Calm, composed and effortlessly sophisticated, Benjamin Moore's Color Trends 2019 15 harmonious hues exude glamour, beauty and balance."
        },
        "2018": {
            "url": "https://www.benjaminmoore.com/-/media/sites/benjaminmoore/files/pdf/color-trends/colortrends2018_usengsp.pdf",
            "description": "Nostalgia gives way to fresh, energetic hues and eye-catching silhouettes, as a classic farmhouse gets a jolt of drama."
        },
        "2017": {
            "url": "https://www.benjaminmoore.com/-/media/sites/benjaminmoore/files/pdf/color-trends/color_trends_2017_us_eng_sp.pdf",
            "description": "23 rich and sophisticated hues ranging from muted pales to saturated deeps."
        },
        "2016": {
            "url": "https://www.benjaminmoore.com/en-us/press/simply-white-2016-color-of-the-year",
            "description": "The color white is transcendent, powerful and polarizing – it is either taken for granted or obsessed over. White is not just a design trend, it is a design essential. The popularity of white, the necessity of white, the mystique of white is quantifiable."
        },
        "2015": {
            "url": "https://media.benjaminmoore.com/WebServices/prod/colortrends2015/offline/download.pdf",
            "description": "Go monochromatic. It's what feels right, right now. Try warm, cool, dark and light layers of the same hue. It's one chromatic concept, gracefully flowing room to room."
        },
        "2014": {
            "url": "https://media.benjaminmoore.com/WebServices/prod/colortrends2014/offline/download.pdf",
            "description": "Breathe. Just breathe. Forget the phones, the screens and the email. Take inspiration from comfort and simplicity. Take a leap and reinvent what you know. Take a moment to exhale. And come home...to a Breath of Fresh Air."
        },
    },
    "Color Families": { # https://www.benjaminmoore.com/en-us/color-overview/color-palettes/color-families/
        "White": {
            "url": "https://www.benjaminmoore.com/en-us/color-overview/color-palettes/color-families/white-paint-colors",
            "description": "Transcendent and timeless, white and off-white paint colors offer unrivaled versatility."
        },
        "Gray": {
            "url": "https://www.benjaminmoore.com/en-us/color-overview/color-palettes/color-families/gray-paint-colors",
            "description": "Equal parts stylish and sensible, gray is a design favorite."
        },
        "Neutral": {
            "url": "https://www.benjaminmoore.com/en-us/color-overview/color-palettes/color-families/neutral-paint-colors",
            "description": "Incredibly versatile and surprisingly complex, neutral paint colors are a homeowner favorite."
        },
        "Blue": {
            "url": "https://www.benjaminmoore.com/en-us/color-overview/color-palettes/color-families/blue-paint-colors",
            "description": "Serenity, tranquility and calm. Ocean, sea and sky. The popularity of blue is palpable."
        },
        "Green": {
            "url": "https://www.benjaminmoore.com/en-us/color-overview/color-palettes/color-families/green-paint-colors",
            "description": "Turn over a new leaf: Benamin Moore offers hundreds of green colors for every style of home, from fresh and mossy hues to deep emeralds and forest greens."
        },
        "Red": {
            "url": "https://www.benjaminmoore.com/en-us/color-overview/color-palettes/color-families/red-paint-colors",
            "description": "From deepest garnet to soft rose, the variety within the red color family always surprises."
        },
        "Black": {
            "url": "https://www.benjaminmoore.com/en-us/color-overview/color-palettes/color-families/black-paint-colors",
            "description": "At first, black paint may feel like a daunting proposition. The reality is that when it comes to any shade of black, the end result is sure to be both unexpected and incredibly sophisticated."
        },
        "Yellow": {
            "url": "https://www.benjaminmoore.com/en-us/color-overview/color-palettes/color-families/yellow-paint-colors",
            "description": "From rich and decadent gold tones, to pale, buttercream hues, yellow paint colors lift spirits while providing warmth and comfort."
        },
        "Pink": {
            "url": "https://www.benjaminmoore.com/en-us/color-overview/color-palettes/color-families/pink-paint-colors",
            "description": "Whether you are looking for a cheerful cherry blossom or an eye-catching fuchsia, pink is a flattering paint color that works wonders in any space."
        },
        "Brown": {
            "url": "https://www.benjaminmoore.com/en-us/color-overview/color-palettes/color-families/brown-paint-colors",
            "description": "Fresh soil, knotted bark, fine sand - the natural tones of brown color schemes evoke back-to-nature vibes. With an organic, easygoing elegance, brown paint colors elevate any room in your home."
        },
        "Orange": {
            "url": "https://www.benjaminmoore.com/en-us/color-overview/color-palettes/color-families/orange-paint-colors",
            "description": "From earthy pumpkin to vibrant and playful summer citrus, orange colors take cues from dynamic aspects of nature–tropical flora, brilliant sunrises, and aromatic spices and seasonings."
        },
        "Purple": {
            "url": "https://www.benjaminmoore.com/en-us/color-overview/color-palettes/color-families/purple-paint-colors",
            "description": "Love a fresh, playful shade of lavender? Or do dark, moody plums speak more to your style? Whether you’re searching for a mood-boosting pastel or a dramatic hue, purple paint colors bring personality to any space."
        },
        "None": {
            "url": "",
            "description": ""
        }
    },
    "Temperature": {
        "Warm": {
            "url": "",
            "description": "Colors that lean towards red"
        },
        "Cool": {
            "url": "",
            "description": "Colors that lean towards blue"
        },
    },
    "Brightness": {
        "Light": {
            "url": "",
            "description": "Light paint colors"
        },
        "Medium": {
            "url": "",
            "description": "Medium-bright paint colors"
        },
        "Dark": {
            "url": "",
            "description": "Dark paint colors"
        },
    },
    "Stains": {
        "Ultra Flat Solid": {
            "url": "https://www.benjaminmoore.com/en-us/product/woodluxe-water-based-deck-siding-exterior-stain-ultra-flat-solid-1-gallon/0695",
            "description" : "Allows the texture of the wood to show through. Offered only in Water-Based Deck + Siding Exterior Stain.",
        },
        "Solid": {
            "url": "https://www.benjaminmoore.com/en-us/product/woodluxe-water-based-deck-siding-exterior-stain-solid-1-gallon/0694",
            "description": "Allows the texture of the wood to show through. Offered only in Water-Based Deck + Siding Exterior Stain."
        },
        "Semi-Solid": {
            "url": "https://www.benjaminmoore.com/en-us/product/woodluxe-water-based-waterproofing-exterior-stain-sealer-semi-solid-1-gallon/0693",
            "description": "Allows the texture and some of the grain pattern of the wood to show through. Offered only in Oil- and Water-Based Waterproofing Exterior Stain + Sealer",
        },
        "Semi-Transparent": {
            "url": "https://www.benjaminmoore.com/en-us/product/woodluxe-water-based-waterproofing-exterior-stain-sealer-semi-transparent-1-gallon/0692",
            "description": "Allows most of the grain pattern and texture of the wood to show through. Offered only in Oil- and Water-Based Waterproofing Exterior Stain + Sealer.",
        },
        "Translucent":
        {
            "url": "https://www.benjaminmoore.com/en-us/product/woodluxe-water-based-waterproofing-exterior-stain-sealer-translucent-1-gallon/0691",
            "description": "Allows the full beauty of the wood to show through. Offered only in Oil- and Water-Based Waterproofing Exterior Stain + Sealer.",
        }
    }
}

missing_groups = []
def add_color_to_group(group_name, color_id):
    group_name = aliases.get(group_name, group_name)

    for category in groups:
        if group_name in groups[category].keys():
            if "colors" not in groups[category][group_name]:
                groups[category][group_name]["colors"] = []
            if id not in groups[category][group_name]["colors"]:
                groups[category][group_name]["colors"].append(id)
            return
    if group_name not in missing_groups:
        missing_groups.append(group_name)
        print("Missing definition for group "+group_name)

for id,color in colors.items():
    # Attibute Groups
    if color["best_selling"]:
        add_color_to_group("Best Selling", id)

    if color["available"]:
        add_color_to_group("Available Online", id)

    if color["exterior"] == "available" or color["exterior"] == "not recommended":
        add_color_to_group("Exterior", id)

    for family in color["families"]:
        add_color_to_group(family, id)

    if color["stains"] != {}:
        add_color_to_group("Wood Stain", id)
    for stain in color["stains"]:
        add_color_to_group(stain, id)

    for palette in color["palettes"]:
        add_color_to_group(palette, id)

    for tag in color["tags"]:
        add_color_to_group(tag, id) 

for cat_name, category in groups.items():
    for group_name,group in category.items():
        if "colors" not in group or group["colors"] == []:
            print(f"{cat_name}->{group_name} has no colors")


print("Writing to groups.json")
with open("../data/groups.json", "w") as fs:
    json.dump(groups, fs, indent=4)

print("Writing to groups.min.json")
with open("../data/groups.min.json", "w") as fs:
    json.dump(groups, fs, separators=(',', ':'))
