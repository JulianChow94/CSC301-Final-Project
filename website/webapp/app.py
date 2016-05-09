from flask import Flask, session, request, redirect, url_for, render_template, flash, jsonify
from flask.ext.triangle import Triangle
from models.database import connection, Tag, Ingredient, Meal
from random import randint
from bson import objectid
from bson.json_util import dumps
from werkzeug.routing import BaseConverter

app = Flask(__name__)
Triangle(app)
mealCol = connection['dev'].meals
tagCol = connection['dev'].tags
ingredientsCol = connection['dev'].ingredients
userCol = connection['dev'].users
app.secret_key = "key"

class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]

'''
	Route urls to functions. Ex. Map @app.route('/users') --> def getUsers().
	One function should be responsible for a url request. 
	To make app.py as clean as possible, any reusable helper functions should 
	be defined in a module, which app.py will import from.
'''

app.url_map.converters['regex'] = RegexConverter

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print "hey"
        print request.form['submit']
        if request.form.get('submit') == 'Find':
            food = request.form.get('food').lower()
            tags = request.form.getlist('tags')

            searchType = request.form.get('searchType')
            sortOption = request.form.get('sort')
            
            
            if searchType == 'ingredientSub':
            	print 'ingredient sub'
            	recommendations = getIngredientSub(food, tags)
            elif searchType == 'mealSub':
            	print 'meals'
            	if sortOption == 'time':
            		foodlist = getMealSub(food, tags)
            		recommendations = _sortCooktime(foodlist)
            	elif sortOption == 'ingredients':
            		foodlist = getMealSub(food, tags)
            		recommendations = _sortIngredients(foodlist)
            	else:
            		recommendations = getMealSub(food, tags)

            #Then we want to return a recomm based on ingredient
            else:

                print 'getmealrecoomm'
                print tags
                recommendations = getMealRecomm(food, tags)
            return render_template('index.html', food=food, recommendations = recommendations)
        else:
            #Surprise me!
            recommCursor = surprise_me()
            recommendation = [recommCursor]
            return render_template('index.html', recommendations=recommendation)

    return render_template("index.html", session=session)


###------------------- LOGIN AND USER FUNCTIONS  ------------------------ ###

@app.route('/userPage')
def getUserPage(username):
    """
    This function takes in the user object passed in from login, extracts
    the user attribute fields from it and passes it towards to userPage Template
    :param user: User object that is passed in from login()
    :return: Template userPage.html with user details passed through
    """
    # Get User Data
    user = userCol.User.find_one({"username": username})
    username = user.username
    email = user.email
    tags = [ each['name'] for each in tagCol.Tag.find({"_id": {"$in" : user.tags}}) if each is not None]
    favourites = [entry for entry in mealCol.Meal.find({"_id" : {"$in" : user.favourites}}) if entry is not None]
    ingloves = [entry for entry in ingredientsCol.Ingredient.find({"_id" : {"$in" : user.ingloves}})
                if entry is not None]
    inghates = [entry for entry in ingredientsCol.Ingredient.find({"_id" : {"$in" : user.inghates}})
                if entry is not None]
    all_tags = [each for each in tagCol.Tag.find() if each is not None]

    # Return the view with data passed in
    return render_template("userPage.html", username=username, email=email, all_tags=all_tags,
                           tags=tags, favourites=favourites, ingloves=ingloves, inghates=inghates)



@app.route('/savetags', methods = ['GET', 'POST'])
def saveTags():
    """
    This function takes all data from the form in userPage.html
    The form hamdles the status of all checkboxes and the submit buttton
    :return: getUserPage funciton that updates the user page
    """
    if request.method == 'POST':
        if request.form['submit'] == 'Save Tags':
            # Get the checked tags
            tags_checked = request.form.getlist('check')

            # Get current user
            userid = request.form['userid']
            current_user = userCol.User.find_one({"username": userid})

            # Update the user's tags
            current_user.tags = [objectid.ObjectId(each) for each in tags_checked if each is not None]
            current_user.save()
            return getUserPage(session['username'])

        elif request.form['submit'] == 'Log Out':
            print("Got Logout button")
            session['logged_in'] = False
            session.clear()
            return redirect(url_for('index'))

@app.route('/profile', methods=['GET', 'POST'])
def login():
    """
    This function takes in the input of 2 field forms in login.html
    and finds a matching user in the database and returns getUserPage
    while creating a Session.
    If no match is found: print an error message and do nothing
    If a match is found but password does not match: also print error
    :return:
    """
    print(session == {})
    if session != {}:
        print("Already Logged In")
        return getUserPage(session['username'])

    elif session == {}:
        print("Not Logged In")
        error = None    # Initialize variable to hold error message
        if request.method == 'POST':

            # Get the POST information
            uname = request.form['username']
            pwd = request.form['password']

            # Get Database information
            match = userCol.User.find_one({"username": uname})

            # Check if username exists
            if match is None:
                print("ConsoleError: User does not exist")
                error = "ERROR: User does not exist"
            # Match found but wrong password
            elif pwd != match.password:
                error = "ERROR: Wrong Password"
            # Otherwise: Login permitted
            else:
                print("Notice: Login Successful!")
                session['username'] = match.username
                session['logged_in'] = True
                flash("Logged In!")
                return getUserPage(match.username)

        return render_template('login.html', error=error)

@app.route("/logout")
def logout():
    """
    This function ends the current session and redirects back to
    the logout view.
    TODO: There is no associated button for this yet
    :return: redirect function to login.html
    """

    print("Logout Acknowledged!")
    session['logged_in'] = False
    session.clear()
    return redirect(url_for('index'))
### ------------------------ END LOGIN AND USER FUNCTIONS ------------------ ###


@app.route('/<regex("\w+"):foodId>', methods=['GET'])
def displayFoodPage(foodId):
    '''Renders view associated with foodId
    Unicode String foodId -> renders view
    '''
    #Use naive method, ie assume that noone will use app maliciously and type object ids that don't exist
    #in URL bar. In this case, the ObjectId will always exist in the DB. Must belong in Ingredient collection
    #or Meal collection

    food = ingredientsCol.Ingredient.find_one({"_id" : objectid.ObjectId(foodId)})
    foodType = 'ingredient';


    if food is None:
        food = mealCol.Meal.find_one({"_id" : objectid.ObjectId(foodId)})
        foodType = 'meal';

    #Hey, tags and alternatives are object ids! You might want to convert them strings
    altNames = list()
    for i in range(len(food['tags'])):
        food['tags'][i] = connection.Tag.find_one({"_id" : food['tags'][i]})['name']

    if foodType == 'meal':
        for i in range(len(food['alter'])):
            food['alter'][i] = connection.Meal.find_one({"_id" : food['alter'][i]})['name']
        for i in range(len(food['ingredients'])):
            food['ingredients'][i] = connection.Ingredient.find_one({"_id" : food['ingredients'][i]})['name']

    else:
        for i in range(len(food['alter'])):
            food['alter'][i] = connection.Ingredient.find_one({"_id" : food['alter'][i]})['name']

    if session:
        user = userCol.User.find_one({"username" : session['username']})
        print food['_id']
        return render_template('foodPage.html', food=food, foodType=foodType, user = user)

    return render_template('foodPage.html', food=food, foodType=foodType)

def getTagNames(tagIds):
    '''Converts a list of tagIds to the corresponding tag names'''
    tagNames = list()

    for tagId in tagIds:
        tag = tagCol.Tag.find_one({"_id" : tagId})
        if tag is not None:
            tagNames.append(tag['name'])
    return tagNames

def getTagIds(tagNames):
    '''Converts a list of tag names to the corresponding tag ids'''
    tagIds = list()
    for tagName in tagNames:
        print tagName
        tag = tagCol.Tag.find_one({"name" : tagName.lower()})
        if tag is not None:
            tagIds.append(tag['_id'])
    return tagIds

def getIngredientSub(ingredient, tagNames):
    '''Returns substitute(s) for given ingredient filtered by tags
        String ingredient , List String tagNames -> List Document substitutes
    '''

    ingredient = ingredientsCol.Ingredient.find_one({"name" : ingredient})
    if ingredient is None:
        return None

    tagIds = getTagIds(tagNames)
    subIds = ingredient['alter']
    substitutes = list()

    for subId in subIds:
            if len(tagIds) > 0:
                #Get alternatives that have tags that exactly match tagIds, or have tags that are a superset of tagIds
                substitute = ingredientsCol.Ingredient.find_one({ "_id" : subId , "tags" : { "$all" : tagIds} })
                if substitute is not None:
                    print substitute
                    substitutes.append(substitute)
            else:
                substitutes.append(ingredientsCol.Ingredient.find_one({"_id" : subId}))

    #Need to display the tag names on result page, so let's replace ObjectIds with names
    for substitute in substitutes:
        substitute['tags'] = getTagNames(substitute['tags'])
        print substitute['tags']
    return substitutes

def getMealSub(meal, tagNames):
    '''Returns substitute(s) for given meal filtered by tags
        String meal , List String tagNames -> List Document substitutes
    '''
    
    meal = mealCol.Meal.find_one({"name" : meal})
    if meal is None:
        return None

    tagIds = getTagIds(tagNames)
    subIds = meal['alter']
    print subIds
    substitutes = list()

    for subId in subIds:
            if len(tagIds) > 0:
                #Get alternatives that have tags that exactly match tagIds, or have tags that are a superset of tagIds
                substitute = mealCol.Meal.find_one({ "_id" : subId , "tags" : { "$all" : tagIds} })
                if substitute is not None:
                    substitutes.append(substitute)
            else:
                substitutes.append(mealCol.Meal.find_one({"_id" : subId}))

    #Need to display the tag names on result page, so let's replace ObjectIds with names
    for substitute in substitutes:
        substitute['num_ingr'] =len(substitute['ingredients'])
        substitute['tags'] = getTagNames(substitute['tags'])

    return substitutes

def getMealRecomm(ingredient, tagNames):
    '''Returns meals that contain that ingredient, filtered by tagNames
        String ingredient, List String tagNames -> List Document recommendations
    '''

    print "hello friend"

    ingredient = ingredientsCol.Ingredient.find_one({"name" : ingredient})
    print ingredient
    if ingredient is None:
        return None

    tagIds = getTagIds(tagNames)
    print tagIds
    
    if len(tagIds) > 0:
        recommendations = list(mealCol.Meal.find({"ingredients" : { "$all" : [ingredient['_id']] } , "tags" : { "$all" : tagIds} }))
    else:
        recommendations = list(mealCol.Meal.find({"ingredients" : { "$all" : [ingredient['_id']] } }))

    #Need to display the tag names on result page, so let's replace ObjectIds with names
    for recommendation in recommendations:
        recommendation['num_ingr'] =len(recommendation['ingredients'])
        recommendation['tags'] = getTagNames(recommendation['tags'])

    return recommendations

@app.route('/addLike', methods=['POST'])
def addLike():
    '''Increments a meal's likedBy field'''

    meal_id = objectid.ObjectId(request.form.get('meal_id'))
    user_id = objectid.ObjectId(request.form.get('user_id'))
    meal = mealCol.Meal.find_one({"_id" : meal_id})
    user = userCol.User.find_one({"_id" : user_id })
    userFavs = user['favourites']
    print userFavs
    userFavs.append(meal_id)
    likedBy = meal['likedby'] + 1

    mealCol.update({"_id": meal_id}, { '$set': { 'likedby': likedBy}})
    userCol.update({"_id" : user_id}, { '$set': { 'favourites': userFavs } })
    print str(meal_id)
    return redirect("/" + str(meal_id))

@app.route('/surprise')
def surprise_me():
    print "surprise_me running!"

    # Surprise me should always return something, even if theres nothing in the database
    # that satisfies the request
    i = 0
    while (i < 15):
        randelement = mealCol.Meal.find_random()
        if 1 > 0: # Incomplete. Should check to see if the tags match the randelement
            break

    print "surprise_me done!"
    randelement['num_ingr'] = len(randelement['ingredients'])
    randelement['tags'] = getTagNames(randelement['tags'])
    return randelement



def _sortIngredients(foodlist):
	sorted_alternative = sorted(foodlist, key = lambda k:len(k['ingredients']))
	return sorted_alternative 

def _sortCooktime(foodlist):
	sorted_alternative = sorted(foodlist, key = lambda k:k['time']['total'])
	return sorted_alternative


if __name__ == '__main__':
    app.run(debug=True)
