"""
Scrape color data off of www.benjaminmoore.com
"""

import requests
import re
import json
from threading import Thread
from bs4 import BeautifulSoup

def get_color_ids():
    colors_xml = requests.get("https://www.benjaminmoore.com/sitemaps/colors.xml", allow_redirects=True).content.decode("utf-8")
    return list(set([m.upper() for m in re.findall(r"https://www.benjaminmoore.com/en-us/paint-colors/color/([A-z0-9\-]+)/", colors_xml)]))

ids = get_color_ids()
colors = list()
def get_color(id):
    print(f"Fetching {id}")
    try:
        r = requests.get("https://www.benjaminmoore.com/en-us/paint-colors/color/"+id, allow_redirects=True)
        html = BeautifulSoup(r.content, features="html.parser")
        jsondata = json.loads(html.find("script", {"id":"__NEXT_DATA__"}).text)["props"]["pageProps"]["componentData"]["components"][0]
        color = jsondata["color_data"]["props"]["color"]
        color["hero_image"] = {
            "large": jsondata["fields"]["hero_image"]["large_url"],
            "medium": jsondata["fields"]["hero_image"]["medium_url"],
            "small": jsondata["fields"]["hero_image"]["small_url"],
            "alt_text": jsondata["fields"]["hero_image"]["alt_text"]
        }
        colors.append(color)

        # Add linked ids
        linked_ids = list()
        if color["aliases"]:
            for alias in color["aliases"].split(", "):
                linked_ids.append(alias)
        for group in color["harmony"]:
            for harmony in group:
                for harmonic in harmony:
                    linked_ids.append(harmonic["number"])
        for similar in color["similar"]:
            linked_ids.append(similar["number"])
        for shade in color["shades"]:
            linked_ids.append(shade["number"])
        for eq in color["equivalent"]:
            linked_ids.append(eq["number"])

        for linked_id in linked_ids:
            if linked_id not in ids:
                ids.append(linked_id)
                print(f"Discovered {linked_id} via {id}")

    except Exception as e:
        print(f"Failed to get {id}: {e}")

def get_color_batch(ids):
    threads = []

    for id in ids:
        thread = Thread(target=get_color, args=(id,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

n = 0
while n < len(ids):
    batch_size = 10
    if n + batch_size > len(ids):
        batch_size = len(ids)-n
    if n % 100 == 0:
        print(f"{n} / {len(ids)}")

    get_color_batch(ids[n:n+batch_size])
    n += batch_size

with open("../data/colors.json", "w") as fs:
    json.dump(colors, fs, indent=4)
