#Use BeautifulSoup4 to Parse an AllRecipes page

import requests
import nltk
from bs4 import BeautifulSoup

from ingredient_transform import measurements, Ingredient, print_ingredient
from utils import string_frac_to_fraction

def parse_recipe(url) -> dict: 
    recipe_items = {}
    #Allows us to imitate a real request more smoothly so rq is not blocked
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        }

    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    #print(soup.prettify())


    #ingredients
    ingredient_objects = soup.find_all("span", class_="ingredients-item-name")
    ingredients_text = [ingredient.getText() for ingredient in ingredient_objects]
    
    #{name: "", quantity value: "", "quantity type: "", prep: ""}
    

    ingredients = []
    for ingredient_text in ingredients_text:
        #init values
        measurement = ""
        amount = ""
        modifier = ""
        name = ""

        #check for an extra special ingrdient modifier (i.e. 1 tsp butter, melted)
        comma_split = ingredient_text.split(", ")
        if len(comma_split) > 1:
            modifier = comma_split[1]

        ingredient_words = comma_split[0].split(' ')
        for i, word in enumerate(ingredient_words):
            if word in measurements:
                measurement = word
                amount = ' '.join(ingredient_words[0:i]).replace("\u2009", "")
                amount = string_frac_to_fraction(amount)

                name = ' '.join(ingredient_words[i+1:])

                ingredients.append( Ingredient(name, amount, measurement, modifier) )
                break 
        
        #If no measurement words are found and loop doesn't break, send an error
        else: 
            print("No measurement found for ingredient: " + ingredient_text)


        

    recipe_items["ingredients"] = ingredients



    #instructions
    instructions_section = soup.find("ul", class_="instructions-section")
    instructions_objects = instructions_section.find_all("p")
    instructions_text = [instruct.getText() for instruct in instructions_objects]
    recipe_items["instructions"] = instructions_text



    #info items
    overview_items = soup.find_all("div", class_="recipe-meta-item-header")
    objects = ["" + item.getText() + " " + item.next_sibling.next_sibling.getText() for item in overview_items]
    recipe_items["overview_items"] = overview_items

    title = soup.find("h1", class_="headline").getText()
    recipe_items["title"] = title

    return recipe_items



#Content to Look at for Transformations
#https://www.allrecipes.com/article/common-ingredient-substitutions/
#https://github.com/rojaswestall/cs337/blob/master/project2/kb.json

#print an ouput of the new recipe
def print_recipe(recipe_items): 
    print("\n-------------")
    print("Recipe: " + recipe_items["title"])
    print("Ingredients: ")
    print("") 

    for ingredient in recipe_items["ingredients"]:
        print_ingredient(ingredient)
    
    print("") 

    print("Steps: ")
    for i, instruction in enumerate(recipe_items["instructions"]): 
        print(str(i) + ". " + instruction + "")

    print("-------------\n")