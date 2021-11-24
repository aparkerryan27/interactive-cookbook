#Use BeautifulSoup4 to Parse an AllRecipes page

import requests
from bs4 import BeautifulSoup
import re #regex expressions

from ingredient_transform import measurements
from utils import string_frac_to_fraction, Ingredient, Recipe

def parse_recipe(url) -> Recipe: 

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


    #Ingredients
    ingredients = []
    ingredient_objects = soup.find_all("span", class_="ingredients-item-name")
    ingredients_text = [ingredient.getText() for ingredient in ingredient_objects]
    for ingredient_text in ingredients_text:
        #init values
        measurement = ""
        amount = ""
        modifier = ""
        name = ""

        #TODO: this will not properly parse "bone-in, skin-on chicken thighs"

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
            amount = string_frac_to_fraction(ingredient_words[0].replace("\u2009", ""))
            name = ' '.join(ingredient_words[1:])

            measurement = "" #no quantifier, direct number of objects required
            ingredients.append(Ingredient(name, amount, measurement, modifier) )



    #Instructions
    instructions_section = soup.find("ul", class_="instructions-section")
    instructions_objects = instructions_section.find_all("p")
    instructions_text = [instruct.getText() for instruct in instructions_objects]

        #Steps?
            #gathering ingredients
            #prep (chopping)
            #cook (fry, sautee)
            #present (put together, plate)
    
    #NOTE: NLTK POS tagger did not work well with these cooking command type of sentences 

    #TODO: verb does not start a sentence in this instance -> "An instant-read thermometer inserted into the thickest part of the thigh should read xxx degrees"
    #TODO: HOW do we get the most significant cooking method out of these?
        #tried to see if the cooking action with the longest duration would be relevant but it is a bad indicator
        
    #Get the verbs (cooking methods) out of all sentences
    cooking_verbs = []
    for instruction in instructions_text:
        sentences = re.split('\. |;', instruction)
        for sentence in sentences:
            words = sentence.split(" ")
            cooking_verbs.append(words[0])


    #Info items
    overview_items = soup.find_all("div", class_="recipe-meta-item-header")
    objects = ["" + item.getText() + " " + item.next_sibling.next_sibling.getText() for item in overview_items]

    title = soup.find("h1", class_="headline").getText()

    return Recipe(title, ingredients, instructions_text, cooking_verbs, objects)
