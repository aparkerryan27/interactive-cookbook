from parsePage import parse_recipe
from utils import print_recipe, convert_recipe_type, scale_recipe

#sample recipe to look at
print('Please provide a recipe link from Allrecipes.com: ')
url = ""
while not url:
    url = input("Recipe URL: ").lower()
    if "allrecipes" not in url:
        print("Invalid URL! Please try again.\n")
        url = ""
# url = "https://www.allrecipes.com/recipe/239230/chef-johns-coq-au-vin/"#"https://www.allrecipes.com/recipe/6698/moms-zucchini-bread/" #"https://www.allrecipes.com/recipe/178630/grandmas-farmhouse-turkey-brine/" 

recipe = parse_recipe(url)
print("Here is your original recipe! ")
print_recipe(recipe)
  
type = input("What type of recipe would you like ? (options: healthy, unhealthy, vegetarian, non-vegetarian, chinese, vegan): ")
type = type.replace(" ", "")

print("Here is your recipe vegetarian", end="")
print(type)
print_recipe(convert_recipe_type(recipe, type))

scaleoption = input("Would you like to increase the number of servings of your recipe? y/N: ")
scaleoption = scaleoption.replace(" ", "")
if scaleoption == "y" or scaleoption == "Y":
    scale = input("How much would you like to increase or decrease your recipe by? (i.e. 1.5, 0.5, 2): ")
    scale_val = float(scale)
    print_recipe(scale_recipe(recipe, scale_val))