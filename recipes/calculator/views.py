from django.shortcuts import render

DATA = {
    "omlet": {
        "яйца, шт": 2,
        "молоко, л": 0.1,
        "соль, ч.л.": 0.5,
    },
    "pasta": {
        "макароны, г": 0.3,
        "сыр, г": 0.05,
    },
    "buter": {
        "хлеб, ломтик": 1,
        "колбаса, ломтик": 1,
        "сыр, ломтик": 1,
        "помидор, ломтик": 1,
    },
}


def recipes(request, name):
    servings = int(request.GET.get("servings", 1))
    try:
        recipe = DATA[name]
        for ingredient, volume in recipe.items():
            recipe[ingredient] = volume * servings
        context = {"recipe": recipe}
    except KeyError:
        context = {"recipe": None}
    return render(request, "calculator/index.html", context)
