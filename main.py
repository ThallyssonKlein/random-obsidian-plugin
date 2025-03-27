import json
import random
import requests
import os

url = "https://raw.githubusercontent.com/obsidianmd/obsidian-releases/HEAD/community-plugins.json"

choosen_files = "./choosen.json"

response = requests.get(url)
if response.status_code != 200:
    print("Error downloading JSON")
    exit()

data = response.json()

if os.path.exists(choosen_files):
    with open(choosen_files, "r") as f:
        choosen = json.load(f)
else:
    choosen = []

available = [item for item in data if item not in choosen]

if not available:
    print("All items have already been chosen!")
    exit()

choosen_item = random.choice(available)
print("Choosen item:", choosen_item)

choosen.append(choosen_item)
with open(choosen_files, "w") as f:
    json.dump(choosen, f, indent=4)
