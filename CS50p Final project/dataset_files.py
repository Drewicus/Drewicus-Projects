import json

def save_dataset(ex, ex_answer):
    with open("dataset.json", "w") as f:
        json.dump({"ex": ex, "ex_answer": ex_answer}, f)
    print("New Data Saved! 🤤 ")

def load_dataset():
    try:
        with open("dataset.json", "r") as f:
            data = json.load(f)
            return data["ex"], data["ex_answer"]
    except FileNotFoundError:

        ex_answer = [
        # Breakfast
        "Fried Rice", "Vegetable Bibimbap", "Paratha", "Chilaquiles", "Croissant",
        "Tamago Kake Gohan", "Pancakes and Bacon", "Scones", "Shakshuka", "Greek Yogurt with Honey",

        # Lunch
        "Spaghetti Carbonara", "Chicken Doner Kebab", "Feijoada", "Lamb Tagine", "Pho Noodles",
        "Green Curry with Rice", "Jerk Chicken", "Pan con Tomate", "Garlic Fried Rice", "Borscht",

        # Dinner
        "Schnitzel", "Piri Piri Chicken", "Injera with Wat", "Kibbeh", "Kebab Koobideh",
        "Seafood Gumbo", "Jollof Rice", "Asado", "Meat Pie", "Fondue",

        # Snacks
        "Pineapple Slices", "Aloo Chaat", "Mohinga", "Momos", "Tsampa",
        "Chirimoya Salad", "Chicken Rezala", "Hummus and Pita", "Bolani", "Plov"
        ]

        ex = [
        ["Breakfast time!", "Chinese", "guilty", "rice", "eat in"],
        ["Breakfast time!", "Korean", "healthy", "vegetables", "eat-out"],
        ["Breakfast time!", "Indian", "guilty", "bread", "eat-in"],
        ["Breakfast time!", "Mexican", "healthy", "grains", "eat-in"],
        ["Breakfast time!", "French", "guilty", "bread", "eat-out"],
        ["Breakfast time!", "Japanese", "healthy", "rice", "eat-in"],
        ["Breakfast time!", "American", "guilty", "meats", "eat-out"],
        ["Breakfast time!", "British", "healthy", "bread", "eat-in"],
        ["Breakfast time!", "Middle Eastern", "guilty", "chicken", "eat-in"],
        ["Breakfast time!", "Greek", "healthy", "dairy", "eat-out"],

        # Lunch
        ["Lunch time!", "Italian", "guilty", "noodles", "eat-in"],
        ["Lunch time!", "Turkish", "healthy", "chicken", "eat-out"],
        ["Lunch time!", "Brazilian", "guilty", "meats", "eat-in"],
        ["Lunch time!", "Moroccan", "healthy", "lamb", "eat-out"],
        ["Lunch time!", "Vietnamese", "guilty", "noodles", "eat-in"],
        ["Lunch time!", "Thai", "healthy", "rice", "eat-out"],
        ["Lunch time!", "Caribbean", "guilty", "chicken", "eat-in"],
        ["Lunch time!", "Spanish", "healthy", "bread", "eat-in"],
        ["Lunch time!", "Filipino", "guilty", "rice", "eat-out"],
        ["Lunch time!", "Russian", "healthy", "vegetables", "eat-in"],

        # Dinner
        ["Dinner time!", "German", "guilty", "meats", "eat-out"],
        ["Dinner time!", "Portuguese", "healthy", "chicken", "eat-in"],
        ["Dinner time!", "Ethiopian", "guilty", "bread", "eat-out"],
        ["Dinner time!", "Lebanese", "healthy", "grains", "eat-in"],
        ["Dinner time!", "Persian", "guilty", "meats", "eat-in"],
        ["Dinner time!", "Cajun", "healthy", "seafood", "eat-out"],
        ["Dinner time!", "African", "guilty", "meats", "eat-in"],
        ["Dinner time!", "Argentinian", "healthy", "meats", "eat-out"],
        ["Dinner time!", "Australian", "guilty", "meats", "eat-in"],
        ["Dinner time!", "Swiss", "healthy", "dairy", "eat-out"],

        # Snacks
        ["Snack time!", "Hawaiian", "guilty", "fruits", "eat-in"],
        ["Snack time!", "Pakistani", "healthy", "vegetables", "eat-out"],
        ["Snack time!", "Burmese", "guilty", "noodles", "eat-in"],
        ["Snack time!", "Nepalese", "healthy", "meats", "eat-out"],
        ["Snack time!", "Tibetan", "guilty", "grains", "eat-in"],
        ["Snack time!", "Chilean", "healthy", "fruits", "eat-out"],
        ["Snack time!", "Bangladeshi", "guilty", "chicken", "eat-in"],
        ["Snack time!", "Israeli", "healthy", "vegetables", "eat-in"],
        ["Snack time!", "Afghan", "guilty", "bread", "eat-out"],
        ["Snack time!", "Uzbek", "healthy", "grains", "eat-in"]
        ]
        return ex, ex_answer


if __name__ == "__main__":
    main()
