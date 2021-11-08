#Use BeautifulSoup4 to Parse an AllRecipes page

import requests
import nltk
from bs4 import BeautifulSoup

#Allows us to imitate a real request more smoothly so rq is not blocked
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

#sample recipe to look at
url = "https://www.allrecipes.com/recipe/21014/good-old-fashioned-pancakes/" 
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')
#print(soup.prettify())


#ingredients
ingredient_objects = soup.find_all("span", class_="ingredients-item-name")
ingredients = [ingredient.getText() for ingredient in ingredient_objects]
print(ingredients)

#instructions
instructions_section = soup.find("ul", class_="instructions-section")
instructions_objects = instructions_section.find_all("p")
instructions_text = [instruct.getText() for instruct in instructions_objects]
print(instructions_text)


#overview items
overview_items = soup.find_all("div", class_="recipe-meta-item-header")
objects = ["" + item.getText() + " " + item.next_sibling.next_sibling.getText() for item in overview_items]
print(objects)
title = soup.find("h1", class_="headline").getText()
print(title)




#Content to Look at for Transformations
#https://www.allrecipes.com/article/common-ingredient-substitutions/



#print an ouput of the new recipe
def print_recipe(): 
    print("Recipe: " + title)
    print("Ingredients: ")
    for i in ingredients:
        print(i + "\n")

    print("\n")
    print("Steps: ")
    for step in len(instructions_text): 
        print(step + ". " + instructions_text[step] + "\n")

    