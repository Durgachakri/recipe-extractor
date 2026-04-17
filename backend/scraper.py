import requests
from bs4 import BeautifulSoup

def extract_recipe(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # TITLE
    title = "No title"
    title_tag = soup.find("h1")
    if title_tag:
        title = title_tag.text.strip()

    # INGREDIENTS
    ingredients = []
    for tag in soup.select("li"):
        text = tag.get_text(strip=True)
        if text and len(text) < 100 and any(char.isdigit() for char in text):
            ingredients.append({
                "quantity": "",
                "unit": "",
                "item": text
            })

    # INSTRUCTIONS
    instructions = []
    for tag in soup.select("p"):
        text = tag.get_text(strip=True)
        if len(text) > 40:
            instructions.append(text)

    if not instructions:
        instructions = ["Instructions not found"]

    return {
        "title": title,
        "ingredients": ingredients[:15],
        "instructions": instructions[:15]
    }