from parsePage import parse_recipe, print_recipe
#sample recipe to look at
url_string = "https://www.allrecipes.com/recipe/6698/moms-zucchini-bread/" #"https://www.allrecipes.com/recipe/178630/grandmas-farmhouse-turkey-brine/" 
recipe = parse_recipe(url_string)
print_recipe(recipe)