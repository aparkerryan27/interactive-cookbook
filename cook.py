from parsePage import parse_recipe, print_recipe
#sample recipe to look at
url_string = "https://www.allrecipes.com/recipe/21014/good-old-fashioned-pancakes/" 
recipe = parse_recipe(url_string)
print_recipe(recipe)