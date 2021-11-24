from unicodedata import numeric
import copy
from ingredient_transform import vegetarian, healthy, x_to_chinese, x_to_non_veg, x_to_non_healthy, to_vegan_list

#Recipe Information
class Recipe:
    def __init__(self, name="Unknown", ingredients=[], directions=[], methods=[], metadata=[]): #, methods=[], tools=[]
        self.name = name
        self.ingredients = ingredients
        self.directions = directions
        self.methods = methods
        self.metadata = metadata
        #self.methods = methods
        #self.tools = tools

def convert_recipe_type(recipe, to_conversion) -> Recipe:
    new_recipe = copy.deepcopy(recipe)

    #To Veggie Conversion
    if to_conversion == "vegetarian":
        for ingredient in new_recipe.ingredients:
            if ingredient.name in vegetarian:
                ingredient.setName(vegetarian[ingredient.name])
    elif type == "unhealthy":
        for ingredient in new_recipe.ingredients:
            if ingredient.name in x_to_non_healthy:
                ingredient.setName(x_to_non_healthy[ingredient.name])
    elif type == "healthy":
        for ingredient in new_recipe.ingredients:
            if ingredient.name in healthy:
                ingredient.setName(healthy[ingredient.name])

    elif type == "non-vegetarian":
        for ingredient in new_recipe.ingredients:
            if ingredient.name in x_to_non_veg:
                ingredient.setName(x_to_non_veg[ingredient.name])
    elif type == "vegan":
        for ingredient in new_recipe.ingredients:
            if ingredient.name in to_vegan_list:
                ingredient.setName(to_vegan_list[ingredient.name])
        
    elif type == "chinese":
        for ingredient in new_recipe.ingredients:
            if ingredient.name in x_to_chinese:
                ingredient.setName(x_to_chinese[ingredient.name])
        

    return new_recipe


#TODO: For our optional conversion, I think we should do common missing ingredient substitutions
#https://www.allrecipes.com/article/common-ingredient-substitutions/


def scale_recipe(recipe, scale) -> Recipe:
    new_recipe = copy.deepcopy(recipe)
    for ingredient in new_recipe.ingredients:
        ingredient.setAmount(ingredient.amount * scale)

    #TODO: (optional improvement) adjust the measurement types after transformation
        #i.e. newly generated 6 teaspoons should just become 2 tablespoons
    return new_recipe

def print_recipe(r: Recipe): 
    print("\n-------------")
    print("Recipe: " + r.name)
    print("Ingredients: ")
    print("") 

    for ingredient in r.ingredients:
        print_ingredient(ingredient)
    
    print("") 

    print("Steps: ")
    for i, instruction in enumerate(r.directions): 
        print(str(i) + ". " + instruction + "")

    print("-------------\n")


#Ingredient Information
class Ingredient:
    def __init__(self, name="ingredient", amount="amount", measurement="measurement", modifier=""):
        self.name = name
        self.amount = amount
        self.measurement = measurement
        self.modifier = modifier

    def setName(self, newname):
        self.name = newname

    def setAmount(self, amount):
        self.amount = amount

def print_ingredient(i: Ingredient):
    #format measurement number as best as possibles
    amount = int(i.amount) if int(i.amount) == float(i.amount) else i.amount 

    #print ingredient information all in one line
    print(str(amount),end=" ")
    if i.measurement:
        print(i.measurement, end=" ")
    print(i.name, end = "")
    if i.modifier:
        print(", " + i.modifier, end="")
    print("\n")

def string_frac_to_fraction(i) -> float:
    if len(i) == 1:
        v = numeric(i)
    elif i[-1].isdigit():
        # normal number, ending in [0-9]
        v = float(i)
    else:
        # Assume the last character is a vulgar fraction
        v = float(i[:-1]) + numeric(i[-1])
    return v