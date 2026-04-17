def generate_nutrition():
    return {
        "calories": 300,
        "protein": "10g",
        "carbs": "40g",
        "fat": "12g"
    }

def generate_substitutions():
    return [
        "Use olive oil instead of butter",
        "Use whole wheat instead of white flour",
        "Use honey instead of sugar"
    ]

def generate_shopping_list(ingredients):
    categories = {"produce": [], "dairy": [], "pantry": []}

    for ing in ingredients:
        item = ing["item"].lower()
        if "milk" in item or "cheese" in item:
            categories["dairy"].append(item)
        elif "tomato" in item or "onion" in item:
            categories["produce"].append(item)
        else:
            categories["pantry"].append(item)

    return categories

def generate_related():
    return ["Pasta", "Salad", "Soup"]