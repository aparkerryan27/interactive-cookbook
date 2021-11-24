
#Ingredient Transformations
#https://github.com/amitadate/EECS-337-NLP-Project-02/blob/master/Final_Submission/transformation_list.py?fbclid=IwAR3kkLEU2g6rs-h6_ujLkpmh6vL4znWXgO-zsUU8BTeoz2ypWNQlMchiRFM

measurements = [
    #Vague
    "dollop",
    "dash",
    "sprinkle",
    "pinch",
    "smidgen",
    "drop",
    
    #Volume
    "teaspoon",
    "teaspoons",
    "t",
    "tsp",

    "tablespoon",
    "tablespoons",
    "T",
    "tbl",
    "tbs",
    "tbsp",
    
    "fluid ounce",
    "fluid ounces",
    "fl oz",
    #"gill",

    "cup",
    "cups",
    "c",

    "pint",
    "pints",
    "p",
    "pt",
    "fl pt",
    "fluid pint", #(Specify Imperial or US)?

    "quart",
    "quarts",
    "q",
    "qt",
    "qts"
    "fl qt",
    "fluid quarts",
    "fluid quart", #(Specify Imperial or US)?

    "gallon",
    "gallons"
    "g", #will this conflict with gram??? 
    "gal",
    "gals"

    "ml",
    "mL",
    "milliliter",
    "milliliters",
    "millilitre",
    "cc",

    "l",
    "liter",
    "liters",
    "litre",
    "L",

    "dl",
    "deciliter",
    "deciliters",
    "decilitre",
    "dL",

    #Mass and Weight,
    "pound",
    "pounds",
    "lb",
    "lbs",

    "ounce",
    "ounces",
    "oz",

    "mg",
    "milligram",
    "milligrams",
    "milligramme",

    "g",
    "gram",
    "grams",
    "gramme",

    "kg",
    "kilogram",
    "kilograms",
    "kilogramme",

    #Length
    "mm",
    "millimeter",
    "millimeters",
    "millimetre",
    
    "cm",
    "centimeter",
    "centimeters",
    "centimetre",

    "m",
    "meter",
    "meters",
    "metre",

    "inch",
    "inches",
    "in",
    "\""

    #TODO: Temperature  ??

'''
Metric Units
Metric units are made up of a base unit and a scale modifier. Each type of measurement has its own base unit. The modifiers are shared between all units. The relevant base units for cooking are:

Mass: gram (g)
Length: meter (m)
Volume: cubic meter (m3)
Commonly used prefix modifiers are:

1/1000 milli (m)
1/100 centi (c)
1/10 deci (d)
100 hecto (h)
1000 kilo (k)
'''
]

#Cooking Relevant Conversions
'''
In cooking the old unit Liter (l) is commonly used to measure volume. One liter is (exactly) equal to 0.001 cubic meters, or 1 cubic decimeter, written like: 1 l = 1 dm3. The prefix modifiers can be used with any unit and thus 1 cl (centiliter) is equal to 1/100 of a liter. The unit for volume is derived from the unit for length. Two lengths forms an area, which is length x length and has the derived unit square meter (m2). Three lengths forms the volume metric m3. This has the consequence that a m3 is equal to 1000 dm3, that is 103 = 10x10x10.

1 l = 10 dl = 100 cl = 1000 ml = 1 dm3 = 0.264 US gallons
1 kg = 10 hg = 1000 g = 2.2 pounds
1 cm = 0.39 inches
Some recipes in Wikibooks Cookbook use American measurement units (pounds and ounces, Fahrenheit, fluid ounces and pints, etc.) and some recipes use metric units (grammes and kilograms, Celsius, milliliter, etc.). An attempt to ensure that all Cookbook recipes use metric units (alone or alongside American units) is an ongoing job. A list of recipes which have been confirmed as having metric units can be found here.

Avoirdupois Conversion Reference
Volume
American (US) units
1 T = 3 t = 1/2 fl oz
2 T = 1 fl oz
1 cup = 16 T = 8 fl oz
1 pint = 2 cups = 16 fl oz
1 qt = 2 pints
1 gal = 4 qt
Mass
1 lb = 16 oz
Mass/Volume conversions
Approximate conversions based on water density. These conversions are useful for more than just water. Although other things have different densities, they are good enough for most estimates.

1 fl oz = 1 oz
1 pint = 1 lb
2 cups = 1 lb
Water has a density of exactly 1 g/cm³

1 mL = 1 g
1 L = 1 kg

'''


healthy = {
    "vegetable oil": "olive oil",
    "potato": "zucchini",
    "canola oil": "olive oil",
    "olive oil": "olive oil",
    "peanut oil": "olive oil",
    "coconut oil": "olive oil",
    "corn oil": "olive oil",
    "sunflower oil": "olive oil",
    "safflower oil": "olive oil",
    "sesame oil" : "olive oil",
    "coconut oil" : "olive oil",
    "oil":"olive oil",
    "whole milk": "low-fat milk",
    "coconut milk" : "almond milk",
    "soy milk" : "almond milk",
    "almond milk" : "almond milk",
    "ice cream": "low-fat frozen yoghurt",
    "whipping cream": "imitation whipped cream(made with skimmed milk)",
    "whipped cream": "imitation whipped cream(made with skimmed milk)",
    "sour cream": "plain low-fat yoghurt",
    "cream cheese": "fat-free cream cheese",
    "american cheese": "fat-free cheese",
    "cottage cheese": "low-fat cottage cheese",
    "mozzarella cheese": "part-skim milk mozzarella cheese",
    "ricotta cheese": "part-skim milk ricotta cheese",
    "granola": "oatmeal",
    "coffee cream": "low-fat milk",
    "ramen noodles": "rice",
    "almond flour": "almond flour",
    "flour": "almond flour",
    "bologna": "low-fat bologna",
    "sausage": "lean ham",
    "vegetable oil": "coconut oil",
    "tortillas": "lettuce leaves",
    "tortilla": "lettuce leaves",
    "couscous": "cauliflower rice",
    "rice": "cauliflower rice",
    "sugar": "stevia",
    "pasta sauce": "almond pesto",
    "penne": "whole wheat penne",
    "linguine": "whole wheat linguine",
    "fettuccine": "whole wheat fettuccine",
    "spaghetti": "spaghetti squash",
    "lasagna": "vegetable lasagna",
    "macaroni": "cauliflower",
    "mac and cheese": "cauliflower and cheese",
    "pasta salad": "mixed vegetables",
    "pasta": "veggie noodles",
    "breadcrumbs": "pork rinds",
    "bread crumbs": "pork rinds",
    "sliced bread": "eggplant",
    "white bread": "whole wheat bread",
    "pancakes": "oatmeal pancakes",
    "pizza crust": "fathead crust",
    "milk": "almond milk",
    "taco shell": "lettuce wrap",
    "french fries": "butternut squash fries",
    "hamburger buns": "portabello mushrooms",
    "burger buns": "portabello mushrooms",
    "buns": "portabello mushrooms",
    "scalloped potatoes": "tempeh",
    "mashed potatoes": "mashed cauliflower",
    "sweet potatoes": "zucchini",
    "potatoes": "zucchini",
    "potato chips": "kale chips",
    "hash browns": "squash",
    "bacon": "fresh pork belly",
    "baking soda": "sodium-free baking soda",
    "barbecue sauce": "low-sodium ketchup",
    "bbq sauce": "low-sodium ketchup",
    "beef jerky": "beef strips",
    "beef noodle soup": "mushroom broth",
    "blue cheese": "part-skim milk mozzarella cheese",
    "bullion": "mushroom broth",
    "camembert cheese": "part-skim milk mozzarella cheese",
    "canned anchovy": "low-sodium sardines",
    "canned corn": "fresh corn",
    "canned tomatoes": "fresh tomatoes",
    "capocollo": "low-sodium ham",
    "chicken noodle soup": "mushroom broth",
    "chicken soup": "mushroom broth",
    "cream of vegetable soup": "mushroom broth",
    "dried beef": "beef strips",
    "feta cheese": "part-skim milk mozzarella cheese",
    "fish sauce": "vinegar",
    "gouda cheese": "part-skim milk mozzarella cheese",
    "hot pepper sauce": "red pepper flakes",
    "instant soup": "mushroom broth",
    "italian salami": "low-sodium ham",
    "ketchup": "low-sodium ketchup",
    "marinade": "flavored vinegar",
    "mayonnaise": "yogurt",
    "mortadella": "low-sodium ham",
    "ground beef": "extra-lean ground beef",
    "olives": "baked grapes",
    "onion soup": "mushroom broth",
    "oyster sauce": "vinegar",
    "paremsan cheese": "part-skim milk mozzarella cheese",
    "pepperoni": "low-sodium ham",
    "pickle": "cucumber",
    "pickled eggplant": "eggplant",
    "pickled peppers": "fresh chiles",
    "prosciutto": "low-sodium ham",
    "queso seco": "part-skim milk mozzarella cheese",
    "ranch dressing": "balsamic vinegar",
    "relish": "low-sodium sweet relish",
    "romano cheese": "part-skim milk mozzarella cheese",
    "roquefort cheese": "part-skim milk mozzarella cheese",
    "salad dressing": "olive oil",
    "salami": "low-sodium ham",
    "salt and pepper": "pepper",
    "salt cod": "fresh cod",
    "salted butter": "unsalted butter",
    "salted mackerel": "fresh mackerel",
    "lightly salted": "",
    "salted": "",
    "sauerkraut": "chopped cabbage",
    "sea salt": "sesame oil",
    "salt": "low-sodium salt substitute",
    "smoked herring": "seared herring",
    "smoked salmon": "fresh salmon",
    "smoked white fish": "seared white fish",
    "soup cube": "mushroom broth",
    "soup": "vegetable puree",
    "soy sauce": "low-sodium soy sauce",
    "steak sauce": "low-sodium steak sauce",
    "stock cube": "mushroom broth",
    "stock": "mushroom broth",
    "table salt": "sesame oil",
    "teriyaki sauce": "vinegar",
    "tomato soup": "mushroom broth",
    "turkey bacon": "fresh turkey strips",
    "turkey salami": "low-sodium ham",
    "vegetable soup": "mushroom broth",
    "chocolate": "carob",
    "beef": "beef(trimmed of external fat)",
    "pork": "lean smoked ham",
    "breaded fish": "unbreaded shellfish",
    "fried fish": "unbreaded shellfish",
    "egg whites":"egg whites",
    "egg white":"egg white",
    "whole eggs": "egg whites",
    "eggs": "egg whites",
    "egg": "egg whites",
    "whole egg": "egg whites",
    "chorizo sausage": "turkey sausage",
    "croissants": "hard french rolls",
    "brioches": "hard french rolls",
    "butter": "whipped butter",
    "avocado": "cucumber slices",
    "margarine": "diet margarine",
    "cheddar cheese": "fat-free cheese",
    "cheese": "low-fat cheese",
    'chilli powder': 'green chilli powder'
}


vegetarian = {
    "chicken bouillon": "vegetable bouillon",
    "beef bouillon": "vegetable bouillon",
    "pork bouillon": "vegetable bouillon",
    "chicken broth": "vegetable broth",
    "chicken stock": "vegetable broth",
    "beef stock": "vegetable broth",
    "beef broth": "vegetable broth",
    "pork stock": "vegetable broth",
    "clam juice": "vegetable broth",
    "fish juice": "vegetable broth",
    "oyster juice": "vegetable broth",
    "ground meat": "textured soy protein",
    "ground beef": "textured soy protein",
    "ground pork": "textured soy protein",
    "pepperoni": "veggie deli slice",
    "pastrami": "veggie deli slice",
    "salami": "veggie deli slice",
    "steak": "portobello mushroom",
    "filet mignon": "portobello mushroom",
    "rib-eye": "portobello mushroom",
    "ribs": "portobello mushroom",
    "burger": "veggie burger",
    "meatball": "veggie meatball",
    "sausage": "veggie sausage",
    "bacon": "veggie bacon",
    "turkey": "soy patties",
    "chicken breast": "seitan tenders",
    "chicken leg": "seitan tenders",
    "chicken thigh": "seitan tenders",
    "chicken nuggets": "soy nuggets",
    "chicken soup":"vegetable soup",
    "chicken": "tofu",
    "jerky": "veggie jerky",
    "pork": "tempeh",
    "meat": "tofurky deli slice",
    "beef": "tofurky deli slice",
    "veal": "tofurky deli slice",
    "lamb": "tofurky deli slice",
    "tuna": "tempeh",
    "tilapia": "tempeh",
    "sardine": "tempeh",
    "salmon": "tempeh",
    "squid": "tempeh",
    "cod": "tempeh",
    "clam": "tempeh",
    "halibut": "tempeh",
    "anchovy": "tempeh",
    "anchovie": "tempeh",
    "mackerel": "tempeh",
    "calamari": "tempeh",
    "shrimp": "tofu",
    "prawn": "tofu",
    "gelatin": "agar flakes",
    "fish": "soy",
    "crab": "tofu"
}

to_vegan_list = {
    "chicken bouillon": "vegetable bouillon",
    "beef bouillon": "vegetable bouillon",
    "pork bouillon": "vegetable bouillon",
    "chicken broth": "vegetable broth",
    "beef broth": "vegetable broth",
    "chicken stock": "vegetable broth",
    "beef stock": "vegetable broth",
    "pork stock": "vegetable broth",
    "pepperoni": "tofurky deli slice",
    "pastrami": "tofurky deli slice",
    "salami": "tofurky deli slice",
    "ribs": "seitan ribs",
    "ground meat": "textured soy protein",
    "ground beef": "textured soy protein",
    "ground pork": "textured soy protein",
    "filet mignon": "portobello mushroom",
    "rib-eye": "portobello mushroom",
    "burger": "veggie burger",
    "meatball": "veggie meatball",
    "sausage": "veggie sausage",
    "chicken breast": "seitan tenders",
    "chicken thigh": "seitan tenders",
    "chicken leg": "seitan tenders",
    "chicken nuggets": "seitan nuggets",
    "chicken": "tofu",
    "pork": "tempeh",
    "jerky": "veggie jerky",
    "tuna": "tempeh",
    "tilapia": "tempeh",
    "sardine": "tempeh",
    "salmon": "tempeh",
    "squid": "tempeh",
    "cod": "tempeh",
    "clam": "tempeh",
    "halibut": "tempeh",
    "anchovy": "tempeh",
    "anchovie": "tempeh",
    "calamari": "tempeh",
    "shrimp": "tofu",
    "prawn": "tofu",
    "milk powder": "almond milk powder",
    "milk": "soy milk",
    "ice cream": "soy ice cream",
    "mozzarella cheese": "vegan mozzarella cheese",
    "mozzarella": "vegan mozzarella",
    "parmesan cheese": "vegan parmesan cheese",
    "cheese": "crumbled tofu",
    "butter": "vegan margarine",
    "yogurt": "almond milk yogurt",
    "scrambled egg": "tofu scramble",
    "egg whites":'tofu',
    "egg white":"tofu",
    "egg yolk": "tofu",
    "egg": "tofu",
    "yolk": "tofu",
    "instant pudding": "dairy free instant pudding",
    "pudding": "dairy free pudding",
    "sour cream": "vegan sour cream",
    "mayonnaise": "vegan mayonnaise",
    "ketchup": "vegan ketchup",
    "gelatin": "agar flakes",
    "honey": "agave nectar",
    "chocolate": "non-dairy chocolate",
    "hollandaise sauce": "vegan hollandaise sauce",
    "oyster sauce": "vegetarian oyster sauce",
    "worcestershire sauce": "organic worcestershire sauce",
    "bread": "wheat tortilla",
    "bread toasts": "wheat tortilla",
    "bagel": "vegan bagel",
    "pancake": "vegan pancake",
    "meat": "tofu",
    "beef": "tempeh",
    "veal": "tofu",
    "lamb": "tempeh",
    "bacon": "vegan bacon",
    "steak": "seitan steak",
    "turkey": "tofurky",
    "fish": "soy",
    "crab": "tofu"
}

x_to_chinese = {
    "olive oil": "peanut oil",
    "burger": " chinese burger",
    "vegetable oil": "peanut oil",
    "canola oil": "peanut oil",
    "peanut oil": "peanut oil",
    "coconut oil": "peanut oil",
    "corn oil": "peanut oil",
    "sunflower oil": "peanut oil",
    "safflower oil": "peanut oil",
    "spaghetti pasta": "lo mein",
    "spaghetti": "lo mein",
    "vinegar": "black vinegar",
    "red pepper flakes": "dried chili pepper",
    "italian parsley": "cilantro",
    "parmigiano-reggiano cheese": "fermented bean curd",
    "penne": "lo mein",
    "mushrooms": "shiitake mushrooms",
    "salad": "malatang",
    "quesadilla": "xian bing",
    "Burger": "chinese hamburger",
    "french pancake": "jian bing",
    "meat sauce": "da lu mian",
    "churro": "you tiao",
    "pizza": "scallion pancake",
    "wine": "shaoxing wine",
    "chicken nuggets": "chicken balls",
    "jerky": "bak kwa",
    "pork": "mapo doufu",
    "meat": "bakkwa",
    "lamb": "lamb broth",
    "pasta": "lo mein",
    "sauce": "hoisin sauce",
    "shrimp": "cha jang mein",
    "tofu": "mapo tofu",
    "white rice": "jasmine scented rice",
    "corn": "bok choy",
    "ice cream": "baobing",
    "tea": "chinese tea",
    "sausage": "lap ceung",
    "salsa" : "mala sauce",
    "maple sauce" : "mala sauce",
    "maple syrup" : "chinese mala syrup"
}

x_to_chinese_utensils = {
    "fork": "chopsticks",
    "frying pan": "wok",
    "pan": "wok",
    "rice cooker": "donabe",
    "cooker": "donabe",
    "spatula": "chuan",
    "ladle": "hoak",
    "pot": "wok",
    "steamers": "bamboo steamers"
}


x_to_non_healthy = {
 'low-fat milk': 'coffee cream',
 'low-fat frozen yoghurt': 'ice cream',
 'yoghurt':'ice cream',
 'imitation whipped cream(made with skimmed milk)': 'whipped cream',
 'skimmed milk':'high fat milk',
 'milk':'whole milk',
 'plain low-fat yoghurt': 'sour cream',
 'fat-free cream cheese': 'cream cheese',
 'fat-free cheese': 'cheddar cheese',
 'low-fat cottage cheese': 'cottage cheese',
 'part-skim milk mozzarella cheese': 'roquefort cheese',
 'part-skim milk ricotta cheese': 'ricotta cheese',
 'cheese':'cheddar cheese',
 'oatmeal': 'granola',
 'rice': 'white rice',
 'almond flour': 'white flour',
 'flour':'white flour',
 'low-fat bologna': 'high-fat bologna',
 'bologna':'high-fat bologna',
 'lean ham': 'sausage',
 'coconut oil': 'mustard oil',
 'olive oil':'mustard oil',
 "vegetable oil": "mustard oil",
    "canola oil": "mustard oil",
    "olive oil": "mustard oil",
    "peanut oil": "mustard oil",
    "coconut oil": "mustard oil",
    "corn oil": "mustard oil",
    "sunflower oil": "mustard oil",
    "safflower oil": "mustard oil",
    "sesame oil" : "mustard oil",
    "coconut oil" : "mustard oil",
    'oil':"mustard oil",
 'oil': 'mustard oil',
 'lettuce leaves': 'cheese tortilla',
 'cauliflower rice': 'white rice',
 'stevia': 'sugar',
 'almond pesto': 'pasta sauce',
 'whole wheat penne': 'penne',
 'whole wheat linguine': 'linguine',
 'whole wheat fettuccine': 'fettuccine',
 'spaghetti squash': 'spaghetti',
 'vegetable lasagna': 'lasagna',
 'cauliflower': 'potatoes',
 'cauliflower and cheese': 'mac and cheese',
 'mixed vegetables': 'fried vegetables',
 'vegetables':'fried vegetables',
 'veggie noodles': 'pasta',
 'pork rinds': 'bread crumbs',
 'eggplant': 'pickled eggplant',
 'whole wheat bread': 'white bread',
 'wheat bread': 'white bread',
 'bread': 'white bread',
 'oatmeal pancakes': 'pancakes',
 'fathead crust': 'pizza crust',
 'almond milk': 'whole milk',
 'lettuce wrap': 'taco shell',
 'butternut squash fries': 'french fries',
 'portabello mushrooms': 'buns',
 'tempeh': 'scalloped potatoes',
 'mashed cauliflower': 'mashed potatoes',
 'zucchini': 'potatoes',
 'kale chips': 'potato chips',
 'squash': 'hash browns',
 'fresh pork belly': 'bacon',
 'sodium-free baking soda': 'baking soda',
 'low-sodium ketchup': 'ketchup',
 'beef strips': 'dried beef',
 'mushroom broth': 'vegetable soup',
 'low-sodium sardines': 'canned anchovy',
 'fresh corn': 'canned corn',
 'fresh tomatoes': 'canned tomatoes',
 'tomatoes': 'canned tomatoes',
 'low-sodium ham': 'turkey salami',
 'vinegar': 'teriyaki sauce',
 'red pepper flakes': 'hot pepper sauce',
 'flavored vinegar': 'marinade',
 'yogurt': 'mayonnaise',
 'extra-lean ground beef': 'ground beef',
 'baked grapes': 'olives',
 'cucumber': 'pickle',
 'fresh chiles': 'pickled peppers',
 'balsamic vinegar': 'ranch dressing',
 'low-sodium sweet relish': 'relish',
 'pepper': 'black pepper',
 'fresh cod': 'salt cod',
 'unsalted butter': 'salted butter',
 'fresh mackerel': 'salted mackerel',
 'chopped cabbage': 'sauerkraut',
 'sesame oil': 'table salt',
 'low-sodium salt substitute': 'salt',
 'salt':'high sodium salt',
 'seared herring': 'fried herring',
 'fresh salmon': 'fried salmon',
 'salmon':'fried salmon',
 'seared white fish': 'fried white fish',
 'fish':'fried fish',
 'vegetable puree': 'soup',
 'low-sodium soy sauce': 'soy sauce',
 'low-sodium steak sauce': 'steak sauce',
 'fresh turkey strips': 'deli meat',
 'turkey strips': 'deli meat',
 'turkey': 'duck',
 'carob': 'chocolate',
 'beef(trimmed of external fat)': 'corned beef',
 'beef':'corned beef',
 'lean smoked ham': 'bacon',
 'ham':'deli meat',
 'chicken':'duck',
 'unbreaded shellfish': 'fried fish',
 'egg whites': 'egg',
 'egg white' : 'egg',
 'turkey sausage': 'chorizo sausage',
 'hard french rolls': 'brioches',
 'whipped butter': 'butter',
 'cucumber slices': 'avocado',
 'diet margarine': 'margarine',
 'low-fat cheese': 'high-fat cheese',
 'sweet potatoes':'potatoes',
 'zucchini':'potatoes',
 'carrots':'glazed carrots',
 'carrot':'glazed carrot',
 'chilli powder': 'red chilli powder',
 'lentils':'fried fish',
 'lentil':'fried fish'
 }

x_to_indian = {
    "salsa" : "tomato chutney",
    "meat" : "chicken",
    "sushi " : "indian sushi",
    'beef': 'chicken',
    'steak': 'chicken',
    'pork': 'mutton',
    'bread': 'naan',
    'noodles': 'rice',
    "olive oil": "peanut oil",
    "burger": " chinese burger",
    "vegetable oil": "sunflower oil",
    "canola oil": "sunflower oil",
    "olive oil": "sunflower oil",
    "peanut oil": "sunflower oil",
    "coconut oil": "sunflower oil",
    "corn oil": "sunflower oil",
    "sunflower oil": "sunflower oil",
    "safflower oil": "sunflower oil",
    "sesame oil" : "sunflower oil",
    "coconut oil" : "sunflower oil",
    'oil':"sunflower oil",
    "spaghetti pasta": "indian maida pasta",
    "spaghetti": "indian maida",
    'pasta': 'rice',
    "vinegar": "indian white vinegar",
    "red pepper flakes": "dried chili pepper",
    "italian parsley": "coriander",
    "parmigiano-reggiano cheese": "fermented paneer",
    "mushrooms": "darjeeling mushrooms",
    "salad": "indian cucumber salad",
    "Burger": "indian hamburger",
    "Meat Sauce": "kheema chutney",
    "Churro": "meetha batter",
    "Pizza": "indian pizza",
    "wine": "sula wine",
    "chicken nuggets": "tandoori chicken balls",
    "meat": "mutton",
    "lamb": "lamb broth",
    "maple sauce" : " chutney",
    "worcestershire sauce" : "tamarind chutney",
    "soy sauce" : "chutney",
    "barbeque sauce" : "chutney",
    "marinara sauce" : "mango chutney",
    "sauce": "chutney",
    "tofu": "paneer",
    "rice": "indian basmati rice",
    "russet potatoes" : "red potatoes",
    "butter" : "amul butter",
    "coconut milk" : "amul milk",
    "soy milk" : "amul milk",
    "almond milk" : "amul milk",
    "milk" : "amul milk",
    "zucchini" : "sweet potatoes"
}


x_to_mexican = {
    'beef': 'carnitas',
    'steak': 'carnitas',
    'fish': 'chicken',
    'bread': 'tortilla',
    'potatoes': 'pinto beans',
    'basil': 'cilantro',
    'parsley': 'cilantro',
    'bell pepper': 'chili pepper',
    'string bean': 'kidney bean',
    'peas': 'black beans',
    'rice': 'quinoa',
    'turnip': 'corn',
    'carrot': 'corn',
    'eggplant': 'tomato',
    'leek': 'onion',
    'garlic': 'onion',
    'parsley': 'cilantro',
    'flour tortillas': 'corn tortillas',
    'mushrooms': 'green peppers',
    'parmesan cheese': 'queso fresco',
    'lemon': 'lime',
    'lemon juice': 'lime juice',
    'coriander': 'paprika',
    'turmeric': 'paprika',
    'teriyaki sauce': 'black mole sauce',
    'ginger root': 'habanero',
    'ginger': 'habanero',
    'olives': 'jalapenos',
    "butter":"compound butter",
    "spinach":"mexican spinach",
    "sweet potato" : "refried beans",
    "potato" : "pinto bean",
    "maple sauce" : " sweet salsa",
    "soy sauce" : "soy salsa",
    "barbeque sauce" : "spicy salsa",
    "marinara sauce" : "salsa",
    "sauce": "salsa"


}

x_to_indian_utensils = {
    "frying pan": "indian frying pan (kadai)",
    "pan": "indian pan (tava)",
    "rice cooker": "pressure cooker",
    "spatula": "indian spatula (palta)",
    "ladle": "indian ladle (degchi)",
    "pot": "indian pot (kadai)",
    "steamers": "bamboo steamers",
    "skillet": "indian pan (kadai)",
    "cooker" : "prestige aluminium cooker"
}

x_to_italian = {
    'rice': 'pasta',
    'noodles': 'pasta',
    'potatoes': 'noodles',
    'potato': 'noodles',
    'corn': 'bell pepper',
    'turnip': 'onion',
    'carrot': 'onion',
    'bok choy': 'lettuce',
    'cilantro': 'basil',
    'chives': 'parsley',
    'jalapeno': 'bell pepper',
    'cayenne': 'bell pepper',
    'ginger': 'garlic'

}

x_to_non_veg = {
    'vegetable bouillon': 'beef bouillon',
    'vegetable broth': 'beef broth',
    'broth' : 'beef broth',
    'textured soy protein': 'ground beef',
    'veggie deli slice': 'salami',
    'veg deli slice': 'salami',
    'vegetarian deli slice': 'salami',
    'portobello mushroom': 'ribs',
    'mushroom':'chicken cubes',
    'veggie burger': 'chicken burger',
    'veg burger':'chicken burger',
    'veggie meatball': 'chicken meatball',
    'veg meatball': 'chicken meatball',
    'veggie sausage': 'chicken sausage',
    'veg sausage': 'chicken sausage',
    'veggie bacon': 'bacon',
    'veg bacon': 'bacon',
    'veggie patties': 'chicken patties',
    'veg patties': 'chicken patties',
    'soy turkey': 'turkey',
    'seitan tenders': 'chicken thigh',
    'soy chicken': 'chicken',
    'soy':'chicken',
    'veggie jerky': 'jerky',
    'tempeh': 'calamari',
    'tofurky deli slice': 'lamb',
    'tofu': 'chicken',
    'paneer':'chicken',
    'agar flakes': 'gelatin',
    'veg soup':'chicken soup',
    'vegetable soup':'chicken soup',
    'potatoes':'chicken cubes',
    'rice cooker':'rice cooker',
    'rice':'chicken rice',
    'pizza':'pepporoni pizza',
    'sweet potatoes':'chicken cubes',
    'sweet potato':'chicken cube',
    'lentils':'fish',
    'lentil':'fish',
    'carrots':'prawns',
    'carrot':'prawn'
 }


{
  "descriptors": {
    "meat": [
      "boneless",
      "hot",
      "instant",
      "lean",
      "lukewarm",
      "raw",
      "refrigerated",
      "skinless",
      "tender",
      "warm"
    ],
    "other": [
      "a la carte",
      "a la king",
      "a la mode",
      "acid",
      "acidic",
      "acrid",
      "airy",
      "alcoholic",
      "ambrosial",
      "aromatic",
      "au fromage",
      "au gratin",
      "au jus",
      "balsamic",
      "bite size",
      "bitter",
      "blah",
      "bland",
      "bold",
      "bolognese",
      "brackish",
      "briny",
      "brittle",
      "bubbly",
      "burning",
      "bursting",
      "buttery",
      "béarnaise",
      "cacciatore",
      "cakey",
      "candied",
      "carmelized",
      "caustic",
      "chalky",
      "charcuterie",
      "cheesy",
      "chewy",
      "chipotle",
      "chocolately",
      "classical",
      "crispy",
      "crumbly",
      "crunchy",
      "crusty",
      "crystalized",
      "curdled",
      "decadent",
      "delactable",
      "dense",
      "diluted",
      "distinctive",
      "doughy",
      "dredged",
      "dried out",
      "dry",
      "earthy",
      "fatty",
      "feathery",
      "fibrous",
      "fiery",
      "filled",
      "filling",
      "finger licking good",
      "fishy",
      "fizzy",
      "flakey",
      "floury",
      "fluffy",
      "folded",
      "fragrant",
      "fresh",
      "fried"
    ],
    "seafood": [
      "cooked",
      "freshly",
      "frozen"
    ],
    "seasoning": [
      "active",
      "all purpose",
      "boiling",
      "distilled",
      "dry",
      "extra firm",
      "extra virgin",
      "frying",
      "ground",
      "heavy",
      "hickory flavored",
      "low sodium",
      "non dairy",
      "nonfat",
      "reduced sodium",
      "room temperature",
      "superfine",
      "sweetened",
      "unsweetened"
    ],
    "style": [
      "african",
      "albanian",
      "algerian",
      "american",
      "andorrian",
      "argentinean",
      "argentinian",
      "armenian",
      "australian",
      "austrian",
      "bangladesh",
      "barbados",
      "belarus",
      "belgian",
      "belize",
      "bolivian",
      "brazilian",
      "british",
      "bulgarian",
      "cambodian",
      "canadian",
      "chad",
      "chilean",
      "chinese",
      "colombian",
      "costa rica",
      "creole",
      "croatian",
      "cuban",
      "dominican",
      "egyptian",
      "el salvadorian",
      "english",
      "estonian",
      "ethiopian",
      "finnish",
      "florentine",
      "french",
      "georgian",
      "german",
      "greek",
      "guatemalan",
      "hungarian",
      "indian",
      "indonesian",
      "iranian",
      "irish",
      "israeli",
      "italian",
      "japanese",
      "kenyan",
      "korean",
      "liberian",
      "libyan",
      "lithuanian",
      "malaysian",
      "mediterranean",
      "mexican",
      "mongolian",
      "moroccan",
      "nigerian",
      "norwegian",
      "peruvian",
      "phillippino",
      "polish",
      "portuguese",
      "puerto rican",
      "romanian",
      "russian",
      "samoan",
      "serbian",
      "sichuan",
      "singapore",
      "slovakian",
      "somalian",
      "south african",
      "spanish",
      "sudanese",
      "swedish",
      "swiss",
      "syrian",
      "szechuan",
      "taiwanese",
      "thai",
      "tunisian",
      "turkish",
      "ukrainian",
      "venezuelan",
      "vietnamese"
    ],
    "veggie": [
      "condensed",
      "fresh",
      "large",
      "organic",
      "packed",
      "ripe",
      "very ripe"
    ]
  },
  "healthy_unhealthy_subs": [
    {
      "healthy": "almond butter",
      "unhealthy": "peanut butter"
    },
    {
      "healthy": "almond milk",
      "unhealthy": "milk"
    },
    {
      "healthy": "almonds",
      "unhealthy": "croutons"
    },
    {
      "healthy": "arrowroot powder",
      "unhealthy": "corn starch"
    },
    {
      "healthy": "avacado",
      "unhealthy": "cheese"
    },
    {
      "healthy": "bacon",
      "unhealthy": "sausage"
    },
    {
      "healthy": "bagels",
      "unhealthy": "english muffins"
    },
    {
      "healthy": "beef stock",
      "unhealthy": "red wine"
    },
    {
      "healthy": "cauliflower",
      "unhealthy": "sweet potatoes"
    },
    {
      "healthy": "chia seeds",
      "unhealthy": "breadcrumbs"
    },
    {
      "healthy": "chicken stock",
      "unhealthy": "white wine"
    },
    {
      "healthy": "cocoa nibs",
      "unhealthy": "chocolate chips"
    },
    {
      "healthy": "coconut cream",
      "unhealthy": "heavy cream"
    },
    {
      "healthy": "coconut flour",
      "unhealthy": "flour"
    },
    {
      "healthy": "coconut oil",
      "unhealthy": "vegetable oil"
    },
    {
      "healthy": "coconut sugar",
      "unhealthy": "brown sugar"
    },
    {
      "healthy": "coconut sugar",
      "unhealthy": "white sugar"
    },
    {
      "healthy": "corn tortilla",
      "unhealthy": "flour tortilla"
    },
    {
      "healthy": "croissant",
      "unhealthy": "muffin"
    },
    {
      "healthy": "egg whites",
      "unhealthy": "eggs"
    },
    {
      "healthy": "fruit-infused water",
      "unhealthy": "fruit juice"
    },
    {
      "healthy": "goat cheese",
      "unhealthy": "low-fat cheese"
    },
    {
      "healthy": "greek yogurt",
      "unhealthy": "sour cream"
    },
    {
      "healthy": "himalayan salt",
      "unhealthy": "table salt"
    },
    {
      "healthy": "honey",
      "unhealthy": "corn syrup"
    },
    {
      "healthy": "hummus",
      "unhealthy": "mayo"
    },
    {
      "healthy": "hummus",
      "unhealthy": "mayonaise"
    },
    {
      "healthy": "kale chips",
      "unhealthy": "pretzels"
    },
    {
      "healthy": "lettuce",
      "unhealthy": "tortillas"
    },
    {
      "healthy": "margarine",
      "unhealthy": "butter"
    },
    {
      "healthy": "mashed cauliflower",
      "unhealthy": "mashed potatoes"
    },
    {
      "healthy": "milk",
      "unhealthy": "creamer"
    },
    {
      "healthy": "mustard",
      "unhealthy": "mayo"
    },
    {
      "healthy": "mustard",
      "unhealthy": "mayonaise"
    },
    {
      "healthy": "nuts",
      "unhealthy": "granola"
    },
    {
      "healthy": "oatmeal",
      "unhealthy": "cereal"
    },
    {
      "healthy": "olive oil and vinegar",
      "unhealthy": "ranch dressing"
    },
    {
      "healthy": "palm shortening",
      "unhealthy": "shortening"
    },
    {
      "healthy": "peanut butter and nutella",
      "unhealthy": "reeses"
    },
    {
      "healthy": "popcorn",
      "unhealthy": "potato chips"
    },
    {
      "healthy": "quinoa",
      "unhealthy": "white rice"
    },
    {
      "healthy": "romaine",
      "unhealthy": "iceberg"
    },
    {
      "healthy": "smashed avacado",
      "unhealthy": "jam"
    },
    {
      "healthy": "smashed avacado",
      "unhealthy": "jelly"
    },
    {
      "healthy": "sprouted toast",
      "unhealthy": "bagel"
    },
    {
      "healthy": "stevia",
      "unhealthy": "sugar"
    },
    {
      "healthy": "tea",
      "unhealthy": "soda"
    },
    {
      "healthy": "tortilla",
      "unhealthy": "pizza dough"
    },
    {
      "healthy": "unrefined powdered sugar",
      "unhealthy": "powdered sugar"
    },
    {
      "healthy": "whole grain pasta",
      "unhealthy": "pasta"
    },
    {
      "healthy": "whole grain spaghetti",
      "unhealthy": "spaghetti"
    },
    {
      "healthy": "whole wheat bread",
      "unhealthy": "white bread"
    },
    {
      "healthy": "zucchini",
      "unhealthy": "noodles"
    }
  ],
  "ingredients": {
    "protein": {
      "anchovies": [],
      "bacon": [],
      "bass": [],
      "beef": [
        "chinese"
      ],
      "beef jerky": [],
      "bison": [],
      "black cod": [],
      "blowfish": [
        "chinese"
      ],
      "bluefish": [],
      "buffalo": [],
      "catfish": [
        "chinese"
      ],
      "caviar": [
        "chinese"
      ],
      "chicken breast": [
        "chinese"
      ],
      "chicken thigh": [
        "chinese"
      ],
      "cod": [
        "chinese"
      ],
      "crab": [
        "chinese"
      ],
      "crayfish": [],
      "cuttlefish": [
        "chinese"
      ],
      "duck": [
        "chinese"
      ],
      "eel": [
        "chinese"
      ],
      "escargot": [],
      "eye of round steak": [],
      "flounder": [
        "chinese"
      ],
      "haddock": [
        "chinese"
      ],
      "halibut": [
        "chinese"
      ],
      "ham": [],
      "herring": [
        "chinese"
      ],
      "hot dog": [],
      "jellyfish": [
        "chinese"
      ],
      "lamb": [
        "chinese"
      ],
      "lamprey": [
        "chinese"
      ],
      "lobster": [
        "chinese"
      ],
      "masago": [],
      "monkfish": [
        "chinese"
      ],
      "mussels": [
        "chinese"
      ],
      "octopus": [
        "chinese"
      ],
      "oyster": [
        "chinese"
      ],
      "pheasant": [
        "chinese"
      ],
      "pike": [
        "chinese"
      ],
      "pork": [
        "chinese"
      ],
      "pork tenderloin": [
        "chinese"
      ],
      "quail": [
        "chinese"
      ],
      "roast beef": [],
      "salmon": [
        "chinese"
      ],
      "scallops": [
        "chinese"
      ],
      "sea cucumber": [
        "chinese"
      ],
      "seitan": [
        "vegetarian"
      ],
      "shark": [
        "chinese"
      ],
      "sheep's meat": [
        "chinese"
      ],
      "shrimp": [
        "chinese"
      ],
      "snails": [
        "chinese"
      ],
      "steak": [],
      "swordfish": [
        "chinese"
      ],
      "tempeh": [
        "chinese",
        "vegetarian"
      ],
      "tilapia": [],
      "tofu": [
        "chinese",
        "vegetarian"
      ],
      "trout": [
        "chinese"
      ],
      "tuna": [
        "chinese"
      ],
      "turkey": [],
      "turkey breast": [],
      "veal": [
        "chinese"
      ],
      "venison": []
    },
    "sauces": {
      "a1 sauce": [],
      "adobo mojado": [],
      "agliata": [],
      "agrodolce": [],
      "aioli": [],
      "ajika": [],
      "ajilimójili": [],
      "ají": [],
      "ají sauce": [],
      "albert sauce": [],
      "alfredo": [],
      "alfredo sauce": [],
      "alioli": [],
      "allemande sauce": [],
      "amatriciana sauce": [],
      "anchovy essence": [],
      "apple sauce": [],
      "arrabbiata sauce": [],
      "au jus": [],
      "avgolemono": [],
      "avocado sauce": [],
      "babi panggang sauce": [],
      "baconnaise": [],
      "bagna càuda": [],
      "bagoong": [],
      "bajan pepper sauce": [],
      "banana ketchup": [],
      "barbecue sauce": [],
      "barese ragù": [],
      "beurre blanc": [],
      "beurre manie": [],
      "beurre monté": [],
      "beurre noir": [],
      "beurre noisette": [],
      "bicky sauce": [],
      "blueberry sauce": [],
      "bolognese": [],
      "bolognese sauce": [],
      "bordelaise sauce": [],
      "bow wow sauce": [
        "chinese"
      ],
      "brasil sauce": [],
      "bread sauce": [],
      "breton sauce": [],
      "brown gravy": [],
      "brown sauce": [],
      "budu": [],
      "buffalo sauce": [],
      "butterscotch sauce": [],
      "béarnaise sauce": [],
      "béchamel sauce": [],
      "café de paris": [],
      "café de paris sauce": [],
      "capital sauce": [],
      "carbonara": [],
      "caruso sauce": [],
      "cebolada": [],
      "chancaca": [],
      "chancho en piedra": [],
      "charcutiere sauce": [],
      "chasseur": [],
      "chateaubriand sauce": [],
      "chaudfroid sauce": [],
      "checca sauce": [],
      "cheddar sauce": [],
      "cheez whiz": [],
      "chermoula": [],
      "chile pepper-tinged sauces": [
        "chinese"
      ],
      "chili sauce": [
        "chinese"
      ],
      "chilli soy lime": [],
      "chimichurri": [],
      "chocolate gravy": [],
      "chocolate syrup": [],
      "cincalok": [],
      "cincinnati chili": [],
      "cocktail sauce": [
        "chinese"
      ],
      "coffee sauce": [],
      "colo-colo": [],
      "comeback sauce": [],
      "condiments portal": [],
      "coney sauce": [],
      "cooked sauces": [],
      "corn sauce": [],
      "coulis": [],
      "cranberry sauce": [],
      "crème anglaise": [],
      "cumberland sauce": [],
      "custard": [],
      "dabu-dabu": [],
      "daddies": [],
      "datil pepper sauce": [],
      "demi glace": [],
      "donair sauce": [],
      "doubanjiang": [
        "chinese"
      ],
      "duck sauce": [
        "chinese"
      ],
      "duckefett": [],
      "egusi sauce": [],
      "enchilada sauce": [],
      "filfel chuma": [],
      "fish sauce": [
        "chinese"
      ],
      "food portal": [],
      "fra diavolo sauce": [],
      "francesinha sauce": [],
      "frankfurt green sauce": [],
      "fritessaus": [],
      "fry sauce": [],
      "fudge sauce": [],
      "garlic sauce": [
        "chinese"
      ],
      "garum": [],
      "gravy": [],
      "gremolata": [],
      "guacamole": [],
      "halford leicestershire table sauce": [],
      "halvaytar": [],
      "hard sauce": [],
      "harissa": [],
      "henry bain sauce": [],
      "hogao": [],
      "hoisin sauce": [],
      "hollandaise sauce": [],
      "honey garlic sauce": [
        "chinese"
      ],
      "horseradish sauce": [],
      "hot sauces": [
        "chinese"
      ],
      "hp sauce": [],
      "huancaina": [
        "chinese"
      ],
      "japanese pickled plum sauce": [],
      "joppiesaus": [],
      "ketchup": [],
      "khrenovina sauce": [],
      "korean soy sauce": [],
      "latik": [],
      "liver sauce": [],
      "llajwa": [],
      "lobster sauce": [
        "chinese"
      ],
      "maafe": [],
      "maggi": [],
      "magic shell": [],
      "mahyawa": [],
      "mala sauce": [
        "chinese"
      ],
      "mango sauce": [
        "chinese"
      ],
      "marie rose sauce": [],
      "marinara sauce": [],
      "melitzanosalata": [],
      "meuniere sauce": [],
      "mignonette sauce": [],
      "mint sauce": [
        "chinese"
      ],
      "mirin": [],
      "moambe": [],
      "mojito isleño": [],
      "mojo": [],
      "mojo criollo": [],
      "mojo sauce": [],
      "mole": [],
      "mornay sauce": [],
      "mostaza la pasiva": [],
      "muhammara": [],
      "mujde": [],
      "mujdei": [],
      "mumbo sauce": [],
      "mushroom gravy": [],
      "mushroom ketchup": [
        "chinese"
      ],
      "mushroom sauce": [],
      "mustard": [],
      "mustard condiment": [],
      "mustard sauces": [],
      "nam chim": [],
      "nam chim gai": [],
      "nam chim seafood": [],
      "nam phrik": [],
      "nantua sauce": [],
      "neapolitan ragù": [],
      "neapolitan sauce": [],
      "normande sauce": [],
      "nước chấm": [],
      "ok sauce": [
        "chinese"
      ],
      "old sour": [],
      "onion gravy": [],
      "onion sauce": [],
      "oxford sauce": [
        "chinese"
      ],
      "oyster sauce": [
        "chinese"
      ],
      "padaek": [],
      "pan sauce": [
        "chinese"
      ],
      "parsley sauce": [],
      "peach sauce": [],
      "peanut sauce": [
        "chinese"
      ],
      "pebre": [],
      "pecel": [],
      "pepper sauces": [
        "chinese"
      ],
      "peppercorn sauce": [
        "chinese"
      ],
      "persillade": [],
      "pesto": [],
      "picadillo": [],
      "picantina": [],
      "pickapeppa sauce": [],
      "pico de gallo": [],
      "pique": [],
      "pique sauce": [],
      "pique verde": [],
      "pla ra": [],
      "plum sauce": [
        "chinese"
      ],
      "ponzu": [],
      "poutine sauce": [],
      "prego": [],
      "prik nam pra": [],
      "ragù": [],
      "ragù alla salsiccia": [],
      "rainbow sauce": [],
      "ravigote": [],
      "ravigote sauce": [],
      "recaíto": [],
      "red-eye gravy": [],
      "redcurrant sauce": [],
      "remoulade": [],
      "romesco": [],
      "romesco sauce": [],
      "rouennaise sauce": [],
      "rouille": [],
      "sahawiq": [],
      "salad cream": [],
      "salad dressing": [],
      "salsa": [],
      "salsa criolla": [],
      "salsa golf": [],
      "salsa lizano": [],
      "salsa verde": [],
      "salvitxada": [],
      "sambal": [],
      "satay sauce": [],
      "satsivi": [],
      "satzibeli": [],
      "sauce africaine": [],
      "sauce allemande": [],
      "sauce américaine": [],
      "sauce andalouse": [],
      "sauce au poivre": [],
      "sauce aurore": [],
      "sauce bercy": [],
      "sauce bourguignonne": [],
      "sauce béchamel": [],
      "sauce charcutière": [],
      "sauce espagnole": [],
      "sauce gribiche": [],
      "sauce hollandaise": [],
      "sauce lyonnaise": [],
      "sauce poivrade": [],
      "sauce poulette": [],
      "sauce robert": [],
      "sauce tomate": [],
      "sauce velouté": [],
      "sauce vierge": [],
      "sauce vin blanc": [],
      "saus cabai": [],
      "sausage gravy": [
        "chinese"
      ],
      "savore sanguino": [],
      "see  green sauce": [],
      "shacha sauce": [],
      "shito": [],
      "shottsuru": [],
      "shrewsbury sauce": [],
      "siu haau sauce": [],
      "skordalia": [],
      "sloppy joe": [],
      "sofrito": [],
      "soubise sauce": [],
      "sour cream sauce": [],
      "soy sauce": [
        "chinese"
      ],
      "sriracha sauce": [],
      "ssamjang": [],
      "steak sauce": [
        "chinese"
      ],
      "strawberry sauce": [
        "chinese"
      ],
      "sugo all'amatriciana": [],
      "sugo alla puttanesca": [],
      "suprême sauce": [],
      "sweet and sour sauce": [
        "chinese"
      ],
      "sweet bean sauce": [
        "chinese"
      ],
      "sweet chili sauce": [
        "chinese"
      ],
      "sweet soy sauce": [
        "chinese"
      ],
      "syrup": [],
      "tabasco sauce": [
        "chinese"
      ],
      "taramasalata": [],
      "tare sauce": [],
      "tartar sauce": [],
      "tentsuyu": [],
      "teriyaki": [],
      "tewkesbury mustard": [],
      "tianmianjiang": [],
      "tkemali": [],
      "tomato sauce": [
        "chinese"
      ],
      "tonkatsu sauce": [],
      "toum": [],
      "tuco": [],
      "tucupi": [],
      "tzatziki": [],
      "tương": [],
      "umeboshi paste": [],
      "velouté sauce": [],
      "venetian sauce": [],
      "vinagrete": [],
      "vinaigrette": [],
      "vincotto": [],
      "vizcaína": [],
      "vodka sauce": [],
      "whisky sauce": [],
      "white sauce": [],
      "wine sauce": [],
      "worcestershire sauce": [],
      "wow-wow sauce": [],
      "xató": [],
      "xo sauce": [
        "chinese"
      ],
      "yogurt sauce": [
        "chinese"
      ],
      "zabaione": [],
      "zigeuner sauce": []
    },
    "spices": {
      "adobo": [],
      "allspice": [],
      "anise extract": ["chinese"],
      "anise seed": ["chinese"],
      "basil": ["chinese"],
      "bay leaf": [
        "chinese"
      ],
      "black pepper": ["chinese"],
      "black peppercorns": ["chinese"],
      "black salt": [],
      "black truffle salt": [],
      "brown sugar": ["chinese"],
      "cajun seasoning": [],
      "calabrian chili peppers": [],
      "cane sugar": [],
      "caraway seeds": [],
      "caraway, ground": [],
      "cardamom": [
        "chinese"
      ],
      "cardamom seeds": [],
      "cayenne pepper": [],
      "chili": ["chinese"],
      "chive": [],
      "cilantro": ["chinese"],
      "cloves": [
        "chinese"
      ],
      "cocoa nibs": [],
      "coriander": ["chinese"],
      "cumin": [],
      "cumin seeds": [],
      "dill": [],
      "dill seed": [],
      "dried chili": [
        "chinese"
      ],
      "fennel": [
        "chinese"
      ],
      "fennel seeds": ["chinese"],
      "garam masala": [],
      "garlic": [
        "chinese"
      ],
      "garlic powder": [
        "chinese"
      ],
      "ghost chili pepper": [],
      "ghost pepper": [],
      "ginger": [
        "chinese"
      ],
      "ginger root": [
        "chinese"
      ],
      "grapefruit": [],
      "green mango": [],
      "green peppercorns": ["chinese"],
      "green serrano chile": [],
      "guajillo chile": [],
      "guajillo chiles": [],
      "habanero": [],
      "habanero pepper": [],
      "honey": ["chinese"],
      "horseradish": [],
      "hot chili": ["chinese"],
      "italian herb seasoning": [],
      "jamaican jerk seasoning": [],
      "juniper berries": ["chinese"],
      "lemon juice": [],
      "lemon peel": [],
      "lemon pepper": [],
      "lemongrass": ["chinese"],
      "lime juice": [],
      "lime peel": [],
      "maple sugar": [],
      "molasses": [],
      "mustard": [],
      "mustard seeds": [],
      "nutmeg": ["chinese"],
      "orange peel": ["chinese"],
      "oregano": ["chinese"],
      "paprika": ["chinese"],
      "parsley": [],
      "parsley flakes": [],
      "peppermint": ["chinese"],
      "rosemary": ["chinese"],
      "saffron": ["chinese"],
      "sage": [],
      "salt": ["chinese"],
      "sassafras": [],
      "sea salt": ["chinese"],
      "sesame seeds": ["chinese"],
      "shallots": ["chinese"],
      "star anise": [
        "chinese"
      ],
      "szechuan peppercorns": [
        "chinese"
      ],
      "tamarind": ["chinese"],
      "tandoori": [],
      "tarragon": ["chinese"],
      "thyme": ["chinese"],
      "turmeric": ["chinese"],
      "vanilla extract": ["chinese"],
      "white pepper": [
        "chinese"
      ]
    },
    "vegetables": {
      "amaranth": [
        "chinese"
      ],
      "amaranth leaves": [
        "chinese"
      ],
      "arrowroot": [],
      "artichoke": [],
      "arugula": [],
      "asparagus": [
        "chinese"
      ],
      "bamboo shoots": [
        "chinese"
      ],
      "beets": [
        "chinese"
      ],
      "belgian endive": [],
      "bitter melon": [],
      "bok choy": [
        "chinese"
      ],
      "broccoli": [
        "chinese"
      ],
      "broccoli rabe": [],
      "brussel sprouts": [],
      "butternut squash": [],
      "carrot": [
        "chinese"
      ],
      "cassava": [],
      "cauliflower": [
        "chinese"
      ],
      "celeriac": [],
      "celery": [
        "chinese"
      ],
      "celery root": [],
      "chayote": [],
      "chicory": [],
      "collards": [],
      "corn": [],
      "crookneck": [],
      "cucumber": [],
      "curly endive": [],
      "daikon": [],
      "dandelion greens": [],
      "edamame": [
        "chinese"
      ],
      "eggplant": [
        "chinese"
      ],
      "fava beans": [],
      "fennel": [],
      "fiddleheads": [],
      "green beans": [
        "chinese"
      ],
      "green cabbage": [
        "chinese"
      ],
      "green onion": [
        "chinese"
      ],
      "green peas": [],
      "green pepper": [
        "chinese"
      ],
      "horseradish": ["chinese"],
      "iceberg lettuce": [],
      "jicama": [],
      "kale": [],
      "kohlrabi": [],
      "leaf lettuce": [],
      "leeks": [],
      "mushrooms": [
        "chinese"
      ],
      "mustard greens": [
        "chinese"
      ],
      "napa cabbage": [
        "chinese"
      ],
      "okra": [
        "chinese"
      ],
      "onions": [
        "chinese"
      ],
      "oysterplant": [],
      "parsnip": [],
      "pea leaves": [
        "chinese"
      ],
      "pea shoots": [
        "chinese"
      ],
      "peas": [
        "chinese"
      ],
      "pumpkin": [],
      "radicchio": [],
      "radishes": [],
      "red cabbage": [
        "chinese"
      ],
      "red onion": [],
      "red pepper": [
        "chinese"
      ],
      "red potato": [
        "chinese"
      ],
      "romaine lettuce": [],
      "rutabaga": [],
      "salsify": [],
      "shallots": [],
      "shepherds purse": [
        "chinese"
      ],
      "snow peas": [
        "chinese"
      ],
      "sorrel": [],
      "soybeans": [
        "chinese"
      ],
      "spaghetti squash": [],
      "spinach": [
        "chinese"
      ],
      "sugar snap peas": [],
      "sweet potato": [
        "chinese"
      ],
      "sweet red pepper": [],
      "swiss chard": [],
      "tomatillo": [],
      "tomato": [
        "chinese"
      ],
      "turnip": [],
      "water spinach": [
        "chinese"
      ],
      "watercress": [
        "chinese"
      ],
      "white potato": [
        "chinese"
      ],
      "yam root": [],
      "yellow onion": [
        "chinese"
      ],
      "yellow potato": [
        "chinese"
      ],
      "yuca root": [],
      "zucchini": []
    }
  },
  "measurements": {
    "liquids": [
      "Tbsp",
      "Tbsps",
      "bottle",
      "bottles",
      "c",
      "cs",
      "cup",
      "cups",
      "dessertspoon",
      "dessertspoons",
      "fl oz",
      "fl ozs",
      "fluid ounce",
      "fluid ounces",
      "fluid oz",
      "fluid ozs",
      "gal",
      "gallon",
      "gallons",
      "gals",
      "jar",
      "jars",
      "liter",
      "liters",
      "milliliter",
      "milliliters",
      "ml",
      "mls",
      "pint",
      "pints",
      "pt",
      "pts",
      "qt",
      "qts",
      "quart",
      "quarts",
      "tablespoon",
      "tablespoons",
      "teaspoon",
      "teaspoons",
      "tsp",
      "tsps"
    ],
    "solids": [
      "#",
      "#s",
      "bag",
      "bags",
      "bunch",
      "bunches",
      "can",
      "cans",
      "clove",
      "cloves",
      "cube",
      "cubes",
      "dash",
      "dashes",
      "envelope",
      "envelopes",
      "gram",
      "grams",
      "head",
      "heads",
      "inch",
      "inches",
      "kilogram",
      "kilograms",
      "lb",
      "lbs",
      "ounce",
      "ounces",
      "oz",
      "ozs",
      "package",
      "packages",
      "packet",
      "packets",
      "piece",
      "pieces",
      "pinch",
      "pinches",
      "pound",
      "pounds",
      "sheet",
      "sheets",
      "slice",
      "slices",
      "strip",
      "strips"
    ]
  },
  "methods": {
    "primary": [
      "bake",
      "boil",
      "broil",
      "fry",
      "pressure cook",
      "grill",
      "mix",
      "simmer",
      "blend",
      "steam"
    ],
    "secondary": [
      "bake",
      "beat",
      "boil",
      "brown",
      "brush",
      "cover",
      "cool",
      "combine",
      "cream",
      "cut",
      "dip",
      "drain",
      "chill",
      "crumble",
      "flour",
      "flip",
      "fold",
      "grease",
      "heat",
      "line",
      "mash",
      "measure",
      "mix",
      "melt",
      "pour",
      "garnish",
      "preheat",
      "pound",
      "layer",
      "stuff",
      "refrigerate",
      "rinse",
      "saute",
      "serve",
      "season",
      "shake",
      "simmer",
      "sift",
      "slice",
      "soak",
      "spoon",
      "spread",
      "sprinkle",
      "stir",
      "strain",
      "toast",
      "toss",
      "turn",
      "whisk"
    ]
  },
  "preparation": {
    "hard_prep": [
      "casings removed",
      "coarsely chopped",
      "dry roasted",
      "finely chopped",
      "finely diced",
      "freeze dried",
      "matchstick cut",
      "roughly chopped",
      "separated florets",
      "thinly sliced"
    ],
    "prep": [
      "al dente",
      "battered",
      "beaten",
      "blackened",
      "blanched",
      "blended",
      "boiled",
      "boned",
      "braised",
      "brewed",
      "broiled",
      "browned",
      "caked",
      "canned",
      "charred",
      "chilled",
      "chopped",
      "cored",
      "creamed",
      "crumbled",
      "crushed",
      "cubed",
      "cured",
      "curried",
      "cut",
      "deglazed",
      "dehydrated",
      "devein",
      "deviled",
      "diced",
      "divided",
      "drained",
      "dried",
      "escalloped",
      "evaporated",
      "fermented",
      "flambé",
      "fricassed",
      "grated",
      "halved",
      "julienned",
      "mashed",
      "melted",
      "minced",
      "peeled",
      "pitted",
      "removed",
      "reserved",
      "rinsed",
      "roasted",
      "rubbed",
      "seasoned",
      "seeded",
      "separated",
      "shredded",
      "sliced",
      "soaked",
      "softened",
      "stemmed",
      "thawed",
      "thawed",
      "torn",
      "unsalted"
    ]
  },
  "scalable": [
    "brown sugar",
    "butter",
    "lard",
    "salt",
    "soy sauce",
    "sugar",
    "white sugar"
  ],
  "tools": [
    "apple corer",
    "apple cutter",
    "bag",
    "baking sheet",
    "balloon whisk",
    "basket skimmer",
    "baster",
    "basting brush",
    "beanpot",
    "bell whisk",
    "bench knife",
    "bench scraper",
    "biscuit mould",
    "blender",
    "blow torch",
    "blowlamp",
    "blowtorch",
    "boil oven preventer",
    "bottle opener",
    "bowl",
    "bread knife",
    "browning bowl",
    "browning plate",
    "browning tray",
    "bulb baster",
    "burger spatula",
    "burr grinder",
    "burr mill",
    "buscuit cutter",
    "buscuit press",
    "butcher's twine",
    "butter curler",
    "cake server",
    "cake shovel",
    "can opener",
    "candy thermometer",
    "carving knife",
    "cheese cutter",
    "cheese grater",
    "cheese knife",
    "cheese knives",
    "cheese slicer",
    "cheese spreader",
    "cheesecloth",
    "chef knife",
    "chef's knife",
    "chefs knife",
    "cherry pitter",
    "chinois",
    "chinoise",
    "citrus reamer",
    "clay pot",
    "cleaver",
    "colander",
    "cookie cutter",
    "cookie mould",
    "cookie press",
    "cooking twine",
    "corkscrew",
    "crab cracker",
    "cup",
    "cutting board",
    "deep spoon",
    "dish",
    "dough scraper",
    "drum sieve",
    "edible tableware",
    "egg piercer",
    "egg poacher",
    "egg separator",
    "egg slicer",
    "egg timer",
    "fat separator",
    "fillet knife",
    "fish scaler",
    "fish slice",
    "fish spatula",
    "flat coil whisk",
    "flat whisk",
    "flour sifter",
    "food mill",
    "food storage container",
    "french whisk",
    "frying pan",
    "funnel",
    "garlic press",
    "grapefruit knife",
    "grater",
    "gravy separator",
    "gravy strainer",
    "gravy whisk",
    "griddle",
    "herb chopper",
    "honey dipper",
    "ice cream scoop",
    "kitchen mallet",
    "kitchen scale",
    "kitchen scissor",
    "kitchen scraper",
    "kitchen string",
    "kitchen tool crock",
    "kitchen twine",
    "knife",
    "ladle",
    "lame",
    "lemon reamer",
    "lemon squeezer",
    "lobster fork",
    "lobster pick",
    "mandoline",
    "mashers",
    "mated colander pot",
    "measuring cup",
    "measuring jar",
    "measuring jug",
    "measuring spoon",
    "meat grinder",
    "meat tenderiser",
    "meat tenderizer",
    "meat thermometer",
    "melon ball",
    "melon baller",
    "metal tong",
    "mezzaluna",
    "microplane",
    "milk frother",
    "milk guard",
    "milk watcher",
    "mincer",
    "mini whisk",
    "mixing bowl",
    "mixing whisk",
    "molcajete",
    "mortar",
    "nutcracker",
    "nutmeg grater",
    "olive stoner",
    "oven glove",
    "oven mitt",
    "oven",
    "pan",
    "panini spatula",
    "pasta fork",
    "pastry bag",
    "pastry blender",
    "pastry brush",
    "pastry wheel",
    "peeler",
    "pepper grinder",
    "pepper mill",
    "pestle",
    "pie bird",
    "pie cutter",
    "pie funnel",
    "pie server",
    "pie vent",
    "pizza cutter",
    "pizza shovel",
    "pizza slicer",
    "pot holder",
    "pot minder",
    "pot",
    "pot-holder",
    "potato masher",
    "potato ricer",
    "potholder",
    "poultry shears",
    "ricer",
    "roast lifter",
    "roller docker",
    "rolling pin",
    "salt shaker",
    "santoku knife",
    "saucepan",
    "scale",
    "scissor",
    "scoop",
    "scraper",
    "serrated bread knife",
    "serving platter",
    "shredder",
    "sieve",
    "sifter",
    "silicone tong",
    "skillet",
    "slotted spoon",
    "spatula",
    "spider strainer",
    "spider",
    "spoon sieve",
    "spoon skimmer",
    "steak knife",
    "stove",
    "strainer",
    "sugar thermometer",
    "tablespoon",
    "tamis",
    "teaspoon",
    "tin opener",
    "tomato knife",
    "tong",
    "trussing needle",
    "turner",
    "twine",
    "urokotori",
    "utility knife",
    "vegetable peeler",
    "weighing scales",
    "whisk",
    "wooden spoon",
    "zester"
  ]
}