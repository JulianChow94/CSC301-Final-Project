from mongokit import Connection
from database import Tag, Ingredient, Meal, User, connection, populateDoc, MONGODB_NAME

def populate( connection):
    for each in ['users','ingredients','meals','tags']:
        connection[MONGODB_NAME].drop_collection(each)

    nutr_dic = { 'cal' : 1, 'fatsat' : 2, 'fatpoly' : 3, 'fatmono' : 4,
            'chol' : 5, 'sodium' : 6, 'pot' : 7, 'carbof' : 8, 'carbos' : 9,
            'iron' : 10, 'mag' : 11, 'va' : 12, 'vb6' : 13, 'vb12' : 14,
            'vc' : 15, 'vd' : 16 }
    #--------------------------------- USERS ---------------------------------
    populateDoc(connection.User, {'username':'admin', 'password' : 'admin', 'email':'bla@bla.bla', 'display':'L33T'})
    populateDoc(connection.User, {'username':'user', 'password' : 'user', 'email':'bla@bla.bla', 'display':'John Smith'})
    populateDoc(connection.User, {'username':'test', 'password' : 'test', 'email':'bla@bla.bla', 'display':'Tester Test'})

    #--------------------------------- TAGS ---------------------------------
    populateDoc(connection.Tag, {'name':'vegan', 'desc':'Why u no eat meat?'})
    populateDoc(connection.Tag, {'name':'working-out', 'desc':'Food that will help you when working out (i.e. have Protein).'})
    populateDoc(connection.Tag, {'name':'low-fat', 'desc':'Only show food low in fats.'})
    populateDoc(connection.Tag, {'name':'gluten-free', 'desc':'Do you even know what that actually means?'})
    populateDoc(connection.Tag, {'name':'meat', 'desc':'The actual source of life, who needs water?'})

    #--------------------------------- GET TAG IDs ---------------------------------
    vegan = connection.Tag.find_one({'name' : 'vegan'})['_id']
    working_out = connection.Tag.find_one({'name' : 'working-out'})['_id']
    gluten_free = connection.Tag.find_one({'name' : 'gluten-free'})['_id']
    low_fat = connection.Tag.find_one({'name' : 'low-fat'})['_id']
    meat = connection.Tag.find_one({'name' : 'meat'})['_id']

    #--------------------------------- INGREDIENTS ---------------------------------
    tags_lst = []
    populateDoc(connection.Ingredient, {'name':'cheddar', 'desc':'Mmmm... Cheesy',
                                        'tags':tags_lst, 'nutrition':nutr_dic})
    tags_lst = [vegan]
    populateDoc(connection.Ingredient, {'name':'macaroni', 'desc':'This might go well with cheese...',
                                        'tags':tags_lst, 'nutrition':nutr_dic})
    tags_lst = [vegan,gluten_free, low_fat]
    populateDoc(connection.Ingredient, {'name':'rice', 'desc':"White/Yellow/Brown, fluffy and nutritious.",
                                        'tags':tags_lst, 'nutrition':nutr_dic})
    tags_lst = [working_out,meat]
    populateDoc(connection.Ingredient, {'name':'ground beef', 'desc':"This cow volunteered to be eaten, vegans.",
                                        'tags':tags_lst, 'nutrition':nutr_dic })
    tags_lst = [working_out,meat,low_fat]
    populateDoc(connection.Ingredient, {'name':'chicken', 'desc':"White meat.",
                                        'tags':tags_lst, 'nutrition':nutr_dic })
    ags_lst = [working_out,meat,low_fat]
    populateDoc(connection.Ingredient, {'name':'turkey', 'desc':"More white meat.",
                                        'tags':tags_lst, 'nutrition':nutr_dic })
    tags_lst = [working_out,meat]
    populateDoc(connection.Ingredient, {'name':'pork', 'desc':"Oink!",
                                        'tags':tags_lst, 'nutrition':nutr_dic})
    tags_lst = [vegan]
    populateDoc(connection.Ingredient, {'name':'spaghetti', 'desc':"Pretty straight-forward...",
                                        'tags':tags_lst, 'nutrition':nutr_dic})
    tags_lst = [vegan,low_fat]
    populateDoc(connection.Ingredient, {'name':'tomato', 'desc':"TomAto, TOmatO...",
                                        'tags':tags_lst, 'nutrition':nutr_dic})
    tags_lst = []
    populateDoc(connection.Ingredient, {'name':'chips', 'desc':"PotAto, POtatO",
                                        'tags':tags_lst, 'nutrition':nutr_dic})
    tags_lst = [low_fat, vegan]
    populateDoc(connection.Ingredient, {'name':'popcorn', 'desc':"*Yoda voice* Pop it goes.",
                                        'tags':tags_lst, 'nutrition':nutr_dic})
    tags_lst = [low_fat, vegan]
    populateDoc(connection.Ingredient, {'name':'bread crumbs', 'desc':"It's bread, just crushed.",
                                        'tags':tags_lst, 'nutrition':nutr_dic})
    tags_lst = [low_fat, vegan, gluten_free]
    populateDoc(connection.Ingredient, {'name':'beans', 'desc':"Beansssss.",
                                        'tags':tags_lst, 'nutrition':nutr_dic})
    tags_lst = [low_fat, vegan, gluten_free]
    populateDoc(connection.Ingredient, {'name':'onion', 'desc':"Tastiest thing to come out of the earth.",
                                        'tags':tags_lst, 'nutrition':nutr_dic})
    tags_lst = [low_fat, vegan, gluten_free]
    populateDoc(connection.Ingredient, {'name':'carrot', 'desc':"Not the tastiest thing to come out of the earth.",
                                        'tags':tags_lst, 'nutrition':nutr_dic})
    tags_lst = [low_fat, vegan, gluten_free]
    populateDoc(connection.Ingredient, {'name':'potato', 'desc':"2nd tastiest thing to come out of the earth.",
                                        'tags':tags_lst, 'nutrition':nutr_dic})
    tags_lst = [low_fat, vegan, gluten_free]
    populateDoc(connection.Ingredient, {'name':'mushroom', 'desc':"Careful which ones you eat!",
                                        'tags':tags_lst, 'nutrition':nutr_dic})
    tags_lst = [low_fat, vegan]
    populateDoc(connection.Ingredient, {'name':'milk', 'desc':"The second source of life.",
                                        'tags':tags_lst, 'nutrition':nutr_dic})
    tags_lst = [low_fat, vegan]
    populateDoc(connection.Ingredient, {'name':'flour', 'desc':"Wanna make bread?",
                                        'tags':tags_lst, 'nutrition':nutr_dic})
    tags_lst = [vegan]
    populateDoc(connection.Ingredient, {'name':'corn', 'desc':"Typical corny stuff.",
                                        'tags':tags_lst, 'nutrition':nutr_dic})
    tags_lst = [vegan]
    populateDoc(connection.Ingredient, {'name':'soy', 'desc':"Some people think its disgusting, its really not.",
                                         'tags':tags_lst, 'nutrition':nutr_dic})
    tags_lst = [meat]
    populateDoc(connection.Ingredient, {'name':'veal', 'desc':"Some people like this stuff :/ .",
                                        'tags':tags_lst, 'nutrition':nutr_dic})

    #--------------------------------- GET INGREDIENTS ---------------------------------
    mac = connection.Ingredient.find_one({'name' : 'macaroni'})
    rice = connection.Ingredient.find_one({'name' : 'rice'})
    spag = connection.Ingredient.find_one({'name' : 'spaghetti'})
    cheddar = connection.Ingredient.find_one({'name' : 'cheddar'})
    grnd_beef = connection.Ingredient.find_one({'name': 'ground beef'})
    chicken =  connection.Ingredient.find_one({'name': 'chicken'})
    turkey =  connection.Ingredient.find_one({'name': 'turkey'})
    pork = connection.Ingredient.find_one({'name':'pork'})
    tomato =  connection.Ingredient.find_one({'name': 'tomato'})
    chips = connection.Ingredient.find_one({'name': 'chips'})
    popcorn = connection.Ingredient.find_one({'name': 'popcorn'})
    breadcrumbs = connection.Ingredient.find_one({'name' : 'bread crumbs'})
    beans = connection.Ingredient.find_one({'name' : 'beans'})
    onion = connection.Ingredient.find_one({'name' : 'onion'})
    potato = connection.Ingredient.find_one({'name' : 'potato'})
    carrot = connection.Ingredient.find_one({'name' : 'carrot'})
    mushroom = connection.Ingredient.find_one({'name' : 'mushroom'})
    milk = connection.Ingredient.find_one({'name' : 'milk'})
    flour = connection.Ingredient.find_one({'name' : 'flour'})
    corn = connection.Ingredient.find_one({'name': 'corn'})
    soy = connection.Ingredient.find_one({'name': 'soy'})
    veal = connection.Ingredient.find_one({'name': 'veal'})

    #--------------------------------- UPDATE INGREDIENTS---------------------------------
    connection.dev.ingredients.update({'name':'macaroni'},{'$set': {'alter':[rice['_id'],spag['_id']]}})
    connection.dev.ingredients.update({'name':'rice'},{'$set': {'alter':[mac['_id'],spag['_id']]}})
    connection.dev.ingredients.update({'name':'spaghetti'},{'$set': {'alter':[mac['_id'],rice['_id']]}})
    connection.dev.ingredients.update({'name':'chicken'},{'$set': {'alter':[grnd_beef['_id'],pork['_id'],turkey['_id']]}})
    connection.dev.ingredients.update({'name':'turkey'},{'$set': {'alter':[grnd_beef['_id'],pork['_id'],chicken['_id']]}})
    connection.dev.ingredients.update({'name':'beans'},{'$set': {'alter':[grnd_beef['_id'],mushroom['_id']]}})
    connection.dev.ingredients.update({'name':'mushroom'},{'$set': {'alter':[grnd_beef['_id'],beans['_id']]}})
    connection.dev.ingredients.update({'name':'pork'},{'$set': {'alter':[grnd_beef['_id'],chicken['_id'],turkey['_id']]}})
    connection.dev.ingredients.update({'name':'ground beef'},{'$set': {'alter':[mushroom['_id'],beans['_id'],chicken['_id'],pork['_id'],turkey['_id']]}})
    connection.dev.ingredients.update({'name':'popcorn'},{'$set': {'alter':[chips['_id']]}})
    connection.dev.ingredients.update({'name':'chips'},{'$set': {'alter':[popcorn['_id']]}})
    connection.dev.ingredients.update({'name':'flour'},{'$set': {'alter':[breadcrumbs['_id']]}})
    connection.dev.ingredients.update({'name':'bread crumbs'},{'$set': {'alter':[flour['_id']]}})

    #--------------------------------- MEALS ---------------------------------
    tags_lst = [vegan]
    ing_lst = [mac['_id'],cheddar['_id']]
    amounts = [500,100]
    populateDoc(connection.Meal, {'name':'macaroni and cheese', 'desc':"America's favourite",
                                        'tags':tags_lst, 'ingredients':ing_lst, 'time': {'total': 25,'prep':10, 'cook':15}, 'likedby':4,'amounts':amounts,
                                        'instructions' : " Boil macaroni for 6-10 minutes until cooked.\n While still hot, throw in cheese and stir.\n Enjoy!"})
    tags_lst = [vegan,gluten_free]
    ing_lst = [potato['_id'],cheddar['_id']]
    amounts = [500,100]
    populateDoc(connection.Meal, {'name':'potatoes and cheese', 'desc':"America's favourite?",
                                        'tags':tags_lst, 'ingredients':ing_lst, 'time': {'total': 25,'prep':10, 'cook':15}, 'likedby':4,'amounts':amounts,
                                        'instructions' : " Boil potatoes for 6-10 minutes until cooked.\n While still hot, throw in cheese and stir.\n Enjoy!"})
    tags_lst = [vegan,gluten_free]
    ing_lst = [carrot['_id'],cheddar['_id']]
    amounts = [500,100]
    populateDoc(connection.Meal, {'name':'carrots and cheese', 'desc':"America's favourite?",
                                        'tags':tags_lst, 'ingredients':ing_lst, 'time': {'total': 25,'prep':10, 'cook':15}, 'likedby':4,'amounts':amounts,
                                        'instructions' : " Boil carrots for 6-10 minutes until cooked.\n While still hot, throw in cheese and stir.\n Enjoy!"})
    tags_lst = [vegan]
    ing_lst = [rice['_id'],cheddar['_id']]
    amounts = [500,100]
    populateDoc(connection.Meal, {'name':'rice and cheese', 'desc':"America's 2nd favourite",
                                        'tags':tags_lst, 'ingredients':ing_lst, 'time': {'total': 30,'prep':10, 'cook':20}, 'likedby':10,'amounts':amounts,
                                        'instructions' : " Boil rice for 8-15 minutes until cooked.\n While still hot, throw in cheese and stir.\n Enjoy!"})
    tags_lst = [vegan, working_out, meat]
    ing_lst = [spag['_id'],grnd_beef['_id']]
    amounts = [500,100]
    populateDoc(connection.Meal, {'name':'spaghetti with beef sauce', 'desc':"Pasta AND meat, finally!",'amounts':amounts,
                                        'tags':tags_lst, 'ingredients':ing_lst, 'time': {'total': 120,'prep':60, 'cook':60}, 'likedby':8})
    tags_lst = [gluten_free, low_fat, meat]
    ing_lst = [rice['_id'],tomato['_id'],chicken['_id']]
    amounts = [500,100,200]
    populateDoc(connection.Meal, {'name':'rice with tomatoes and chicken', 'desc':"Tomatoey goodness.",'amounts':amounts,
                                        'tags':tags_lst, 'ingredients':ing_lst, 'time': {'total': 120,'prep':60, 'cook':60}})
    tags_lst = [vegan]
    ing_lst = [popcorn['_id'],soy['_id']]
    amounts = [100,20]
    populateDoc(connection.Meal, {'name':'Popcorn dipped in soy sauce ;)', 'desc':"some weird corn + soy stuff",'amounts':amounts,
                                        'tags':tags_lst, 'ingredients':ing_lst, 'time': {'total': 5,'prep':1, 'cook':4}})

    tags_lst = [meat, working_out]
    ing_lst = [chicken['_id'],milk['_id'],flour['_id']]
    amounts = [300,100,200]
    populateDoc(connection.Meal, {'name':'fried chicken', 'desc':"Is it wings?",'amounts':amounts,
                                        'tags':tags_lst, 'ingredients':ing_lst, 'time': {'total': 50,'prep':20, 'cook':30}, 'likedby':8,
                                        'instructions' : "Dip chicken tenders in milk.\nCover them in flour\nFry them for 20 minutes(10-minutes each side)\nEnjoy!"})
    tags_lst = [meat, working_out]
    ing_lst = [turkey['_id'],milk['_id'],flour['_id']]
    amounts = [300,100,200]
    populateDoc(connection.Meal, {'name':'grilled turkey', 'desc':"Is it wings?",'amounts':amounts,
                                        'tags':tags_lst, 'ingredients':ing_lst, 'time': {'total': 40,'prep':20, 'cook':20}, 'likedby':5,
                                        'instructions' : "Grill turkey for 20 minutes(10-minutes each side)\nEnjoy!"})
    tags_lst = [meat, low_fat]
    ing_lst = [chicken['_id'],milk['_id'],flour['_id']]
    amounts = [500,100,100]
    populateDoc(connection.Meal, {'name':'baked chicken', 'desc':"Is it not wings?",'amounts':amounts,
                                        'tags':tags_lst, 'ingredients':ing_lst, 'time': {'total': 40,'prep':20, 'cook':30}, 'likedby':6,
                                        'instructions' : "Dip chicken tenders in milk.\nCover them in flour\nBake them for 30 minutes(15-minutes each side)\nEnjoy!"})
    tags_lst = [meat, low_fat]
    ing_lst = [chicken['_id']]
    amounts = [500]
    populateDoc(connection.Meal, {'name':'steamed chicken', 'desc':"Is it not wings?",'amounts':amounts,
                                        'tags':tags_lst, 'ingredients':ing_lst, 'time': {'total': 40,'prep':20, 'cook':30}, 'likedby':4,
                                        'instructions' : "Boil chicken tenders in water for 30 minutes\nEnjoy!"})


    #--------------------------------- Burgers ---------------------------------

    tags_lst = [vegan, gluten_free, low_fat]
    ing_lst = [beans['_id'],rice['_id'],onion['_id'],breadcrumbs['_id']]
    amounts = [500,100,100,20]
    populateDoc(connection.Meal, {'name':'veggie burger', 'desc':"A popular twist on the classic Hamburger.",'amounts':amounts,
                                        'tags':tags_lst, 'ingredients':ing_lst, 'time': {'total': 40,'prep':20, 'cook':20}, 'likedby':8,
                                        'instructions' : " Mix all the ingredients together, adding salt to taste.\n Cut large pieces and shape them to your tastes.\n Grill for 20 minutes (10-minutes each side)."})

    tags_lst = [working_out, meat]
    ing_lst = [grnd_beef['_id'],onion['_id'],breadcrumbs['_id']]
    amounts = [500,100,20]
    populateDoc(connection.Meal, {'name':'hamburger', 'desc':"You must have heard of it.",'amounts':amounts,
                                        'tags':tags_lst, 'ingredients':ing_lst, 'time': {'total': 50,'prep':20, 'cook':30}, 'likedby':10,
                                        'instructions' : " Mix all the ingredients together, adding salt to taste.\n Cut large pieces and shape them to your tastes.\n Grill for 20 minutes (10-minutes each side)."})
    tags_lst = [working_out, meat]
    ing_lst = [pork['_id'],onion['_id'],breadcrumbs['_id']]
    amounts = [500,100,20]
    populateDoc(connection.Meal, {'name':'porkburger', 'desc':"Does pork work?.",'amounts':amounts,
                                        'tags':tags_lst, 'ingredients':ing_lst, 'time': {'total': 50,'prep':20, 'cook':30}, 'likedby':4,
                                        'instructions' : " Mix all the ingredients together, adding salt to taste.\n Cut large pieces and shape them to your tastes.\n Grill for 20 minutes (10-minutes each side)."})

    tags_lst = [vegan, gluten_free, low_fat]
    ing_lst = [mushroom['_id'],onion['_id'],breadcrumbs['_id']]
    amounts = [500,100,20]
    populateDoc(connection.Meal, {'name':'mushroom burger', 'desc':"A popular twist on the classic Hamburger.",'amounts':amounts,
                                        'tags':tags_lst, 'ingredients':ing_lst, 'time': {'total': 15,'prep':5, 'cook':10}, 'likedby':6,
                                        'instructions' : " Mix all the ingredients together, adding salt to taste.\n Cut large pieces and shape them to your tastes.\n Grill for 20 minutes (10-minutes each side)."})

    tags_lst = [meat, low_fat]
    ing_lst = [chicken['_id'],onion['_id'],breadcrumbs['_id']]
    amounts = [500,100,20]
    populateDoc(connection.Meal, {'name':'chicken burger', 'desc':"A popular twist on the classic Hamburger.",'amounts':amounts,
                                        'tags':tags_lst, 'ingredients':ing_lst, 'time': {'total': 50,'prep':20, 'cook':30}, 'likedby':9,
                                        'instructions' : " Mix all the ingredients together, adding salt to taste.\n Cut large pieces and shape them to your tastes.\n Grill for 20 minutes (10-minutes each side)."})
    tags_lst = [vegan, gluten_free, low_fat]
    ing_lst = [carrot['_id'],onion['_id'],breadcrumbs['_id']]
    amounts = [500,100,20]
    populateDoc(connection.Meal, {'name':'carrot burger', 'desc':"A popular twist on the classic Hamburger.",'amounts':amounts,
                                        'tags':tags_lst, 'ingredients':ing_lst, 'time': {'total': 50,'prep':20, 'cook':30}, 'likedby':3,
                                        'instructions' : " Mix all the ingredients together, adding salt to taste.\n Cut large pieces and shape them to your tastes.\n Grill for 20 minutes (10-minutes each side)."})

    #--------------------------------- Salad ---------------------------------
    tags_lst = [meat, low_fat, working_out]
    ing_lst = [chicken['_id'],onion['_id'],tomato['_id']]
    amounts = [500,100,20]
    populateDoc(connection.Meal, {'name':'chicken salad', 'desc':"Chicken salad.",'amounts':amounts,
                                        'tags':tags_lst, 'ingredients':ing_lst, 'time': {'total': 40,'prep':10, 'cook':30}, 'likedby':6,
                                        'instructions' : " Mix all the ingredients together, adding salt to taste.\n Cut large pieces and shape them to your tastes.\n Grill for 20 minutes (10-minutes each side)."})

    chickensalad = connection.Meal.find_one({'name': 'chicken salad'})


    macncheese = connection.Meal.find_one({'name': 'macaroni and cheese'})
    ricencheese = connection.Meal.find_one({'name': 'rice and cheese'})
    potatoesncheese = connection.Meal.find_one({'name': 'potatoes and cheese'})
    carrotsncheese = connection.Meal.find_one({'name': 'carrots and cheese'})

    hamburger = connection.Meal.find_one({'name': 'hamburger'})
    porkburger = connection.Meal.find_one({'name': 'porkburger'})
    veggieburger = connection.Meal.find_one({'name': 'veggie burger'})
    mushroomburger = connection.Meal.find_one({'name': 'mushroom burger'})
    chickenburger = connection.Meal.find_one({'name': 'chicken burger'})
    carrotburger = connection.Meal.find_one({'name': 'carrot burger'})

    friedchicken = connection.Meal.find_one({'name': 'fried chicken'})
    bakedchicken = connection.Meal.find_one({'name': 'baked chicken'})
    steamedchicken = connection.Meal.find_one({'name': 'steamed chicken'})
    grilledturkey = connection.Meal.find_one({'name': 'grilled turkey'})

    connection.dev.meals.update({'name':'rice and cheese'},{'$set': {'alter':[macncheese['_id'],potatoesncheese['_id'],carrotsncheese['_id']]}})
    connection.dev.meals.update({'name':'macaroni and cheese'},{'$set': {'alter':[ricencheese['_id'],potatoesncheese['_id'],carrotsncheese['_id']]}})
    connection.dev.meals.update({'name':'potatoes and cheese'},{'$set': {'alter':[ricencheese['_id'],macncheese['_id'],carrotsncheese['_id']]}})
    connection.dev.meals.update({'name':'carrots and cheese'},{'$set': {'alter':[ricencheese['_id'],potatoesncheese['_id'],macncheese['_id']]}})

    connection.dev.meals.update({'name':'fried chicken'},{'$set': {'alter':[bakedchicken['_id'],steamedchicken['_id'],grilledturkey['_id']]}})
    connection.dev.meals.update({'name':'baked chicken'},{'$set': {'alter':[friedchicken['_id'],steamedchicken['_id'],grilledturkey['_id']]}})
    connection.dev.meals.update({'name':'steamed chicken'},{'$set': {'alter':[friedchicken['_id'],bakedchicken['_id'],grilledturkey['_id']]}})
    connection.dev.meals.update({'name':'grilled turkey'},{'$set': {'alter':[friedchicken['_id'],steamedchicken['_id'],bakedchicken['_id']]}})

    connection.dev.meals.update({'name':'hamburger'},{'$set': {'alter':[veggieburger['_id'],mushroomburger['_id'],chickenburger['_id'],porkburger['_id'],carrotburger['_id']]}})
    connection.dev.meals.update({'name':'veggie burger'},{'$set': {'alter':[hamburger['_id'],mushroomburger['_id'],porkburger['_id'],chickenburger['_id'],carrotburger['_id']]}})
    connection.dev.meals.update({'name':'mushroom burger'},{'$set': {'alter':[veggieburger['_id'],hamburger['_id'],porkburger['_id'],chickenburger['_id'],carrotburger['_id']]}})
    connection.dev.meals.update({'name':'chicken burger'},{'$set': {'alter':[veggieburger['_id'],hamburger['_id'],porkburger['_id'],mushroomburger['_id'],carrotburger['_id']]}})
    connection.dev.meals.update({'name':'porkburger'},{'$set': {'alter':[veggieburger['_id'],hamburger['_id'],chickenburger['_id'],mushroomburger['_id'],carrotburger['_id']]}})
    connection.dev.meals.update({'name':'carrot burger'},{'$set': {'alter':[veggieburger['_id'],hamburger['_id'],chickenburger['_id'],mushroomburger['_id'],porkburger['_id']]}})

    connection.dev.meals.update({'name':'chicken salad'},{'$set': {'alter':[chickenburger['_id'],hamburger['_id']]}})



if __name__=='__main__':
    print "populating"
    populate(connection)
