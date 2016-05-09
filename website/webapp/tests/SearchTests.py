import unittest
from flask import Flask
from ..app import getRecommendations, _sortIngredients, _sortCooktime
from .. models.database import connection, Tag, Ingredient, Meal
from scipy.optimize.zeros import results_c



#setup db connection for unit tests
mealCol = connection['dev'].meals
tagCol = connection['dev'].tags
ingredientsCol = connection['dev'].ingredients
test_db = connection['dev']

class GetRecommendationsHelperTestCase(unittest.TestCase):
	def setUp(self):
		#NEED models: Meal, Ingredients, Tags
		#Note: Databases and Collections are created lazily
		#Populate db with meals, ingredients, tags
		highFatTag = connection.Tag()
		highFatTag.name = "high fat"
		highFatTag.save()
		highFatTagId = tagCol.Tag.find_one({"name" : highFatTag.name})['_id']
		veganTag = connection.Tag()
		veganTag.name = "vegan"
		veganTag.save()
		veganId = tagCol.Tag.find_one({"name" : veganTag.name})['_id']
		rice = connection.Ingredient()
		rice.name = 'rice'
		rice.tags = [veganId]
		rice.save()
		riceId = ingredientsCol.Ingredient.find_one({"name" : rice.name})['_id']
		eggs = connection.Ingredient()
		eggs.name = "eggs"
		eggs.save()
		eggsId = ingredientsCol.Ingredient.find_one({"name" : eggs.name})['_id']
		macaroni = connection.Ingredient()
		macaroni.name = 'macaroni'
		macaroni.tags = [veganId]
		macaroni.alter = [riceId, eggsId]
		macaroni.save()
		cheese = connection.Ingredient()
		cheese.name = 'cheese'
		cheese.tags = [veganId]
		cheese.save()
		macId = ingredientsCol.Ingredient.find_one({"name" : macaroni.name})['_id']
		cheeseId = ingredientsCol.Ingredient.find_one({"name" : cheese.name})['_id']
		macNCheese = connection.Meal()
		macNCheese.name = 'Mac and Cheese'
		macNCheese.ingredients = [macId, cheeseId]
		macNCheese.tags = [veganId, highFatTagId]
		macNCheese.save()
		
		#adding some more setups -roy
		bun = connection.Ingredient()
		bun.name = 'bun'
		bun.tags = [veganId]
		bun.save()
		bunId = ingredientsCol.Ingredient.find_one({'name':'bun'})['_id']
		veggiepatty = connection.Ingredient()
		veggiepatty.name = 'veggiepatty'
		veggiepatty.tags = [veganId]
		veggiepatty.save()
		veggiepattyId = ingredientsCol.Ingredient.find_one({'name':'veggiepatty'})['_id']
		
		#assume cheese is vegan LOL!
		
		veggieBurger = connection.Meal()
		veggieBurger.name = 'Veggie Burger'
		veggieBurger.ingredients = [cheeseId, veggiepattyId,bunId] # 3 ingredients
		veggieBurger.tags = [veganId]
		veggieBurger.time = { 'total': 100, 'prep' : 30 ,'cook' : 70 }
		veggieBurger.save()
		vbId = mealCol.Ingredient.find_one({"name" : veggieBurger.name})['_id']
		
		veggieBurger1 = connection.Meal()
		veggieBurger1.name = 'Veggie Burger1'
		veggieBurger1.ingredients = [cheeseId, bunId] # 2 ingredients 
		veggieBurger1.tags = [veganId]	
		veggieBurger1.time = { 'total': 50, 'prep' : 20 ,'cook' : 30 }	
		veggieBurger1.save()
		vb1Id = mealCol.Ingredient.find_one({"name" : veggieBurger1.name})['_id']
		
		veggieBurger2 = connection.Meal()
		veggieBurger2.name = 'Veggie Burger2'
		veggieBurger2.ingredients = [cheeseId,macId,veggiepattyId,bunId] # 4 ingredients
		veggieBurger2.tags = [veganId]
		veggieBurger2.alter = [vbId, vb1Id]
		veggieBurger2.save()
		vb2Id = mealCol.Ingredient.find_one({"name" : veggieBurger2.name})['_id']

		

	def tearDown(self):
		'''delete the collections'''
		test_db.drop_collection('meals')
		test_db.drop_collection('ingredients')
		test_db.drop_collection('tags')

	def testHasRecommWithTag(self):
		cursor = getRecommendations("macaroni", ["vegan"])
		results = []
		self.assertIsNotNone(cursor)
		for element in cursor:
			results.append(element['name'])
		expected = ['rice']
		self.assertEqual(results, expected)
	
	def testHasRecommNoTag(self):
		cursor = getRecommendations("macaroni", [])
		results = []
		self.assertIsNotNone(cursor)
		for element in cursor:
			results.append(element['name'])
		expected = ['rice', 'eggs']
		self.assertEqual(results, expected)

	def testNoRecommendation(self):
		cursor = getRecommendations("Hamburger", [])
		self.assertEqual(cursor, None)

	def testNoTagMatch(self):
		cursor = getRecommendations("Hamburger", ["nope"])
		self.assertEqual(cursor, None)
		
		
		
	#this is sorting test	
	def testMultipleMeals_Sort_ingr(self):
		cursor = getRecommendations("Veggie Burger2", ["vegan"],'ingredients')
		self.assertIsNotNone(cursor)
		sorted = _sortIngredients(cursor)
		expected = 2
		result = len(sorted[0]['ingredients'])
		self.assertEqual(result, expected)
		
	def testMultipleMeals_Sort_time(self):
		cursor = getRecommendations("Veggie Burger2", ["vegan"],'time')
		self.assertIsNotNone(cursor)
		sorted = _sortCooktime(cursor)
		print cursor
		print sorted
		expected = 50
		result = sorted[0]['time']['total']
		self.assertEqual(result, expected)
		
if __name__ == '__main__':
	unittest.main()
