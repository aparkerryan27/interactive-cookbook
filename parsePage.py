import requests
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

ingredient_objects = soup.find_all("span", class_="ingredients-item-name")
ingredients = [ingredient.getText() for ingredient in ingredient_objects]
print(ingredients)

instructions_section = soup.find("ul", class_="instructions-section")
instructions_objects = instructions_section.find_all("p")
instructions_text = [instruct.getText() for instruct in instructions_objects]
print(instructions_text)


