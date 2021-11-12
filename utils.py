from unicodedata import numeric
import copy
from ingredient_transform import vegetarian

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
    if to_conversion == "vegetarian":
        for ingredient in new_recipe.ingredients:
            if ingredient.name in vegetarian:
                ingredient.setName(vegetarian[ingredient.name])
            else:
                print("ERROR: no " + to_conversion + " conversion found for: ", end="")
                print(ingredient.name)

    return new_recipe

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