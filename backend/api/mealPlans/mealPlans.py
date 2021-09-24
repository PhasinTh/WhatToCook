from flask import request
from flask_restful import Resource
from settings import redisConnection, GenerateMealPlan
import uuid
import json




class MealPlans(Resource):

    def __init__ (self, **kwargs):
        self.ingredientList = kwargs["ingredientList"]
        self.recipeList = kwargs["recipeList"]
        self.purchaseableList = kwargs["purchaseableList"]
        self.rawIngredients = kwargs["rawIngredients"]

    def post(self):
        taskId = uuid.uuid1()
        data = request.get_json()
        numberOfMeal = data["numberOfMeal"]
        ingredients = data["ingredients"]
        caloriesPreference = data["caloriesPreference"]
        costPreference = data["costPreference"]
        GenerateMealPlan.delay(
            taskId, 
            caloriesPreference, 
            costPreference, 
            numberOfMeal, 
            self.recipeList, 
            self.ingredientList, 
            self.purchaseableList,
            self.rawIngredients,
            {"basket": ingredients}
        )
        return {"id": str(taskId)}
    
class MealPlan(Resource):

    def get(self, id):
        mealPlan = redisConnection.get(id)
        if mealPlan == None:
            return {}
        else:
            return json.loads(mealPlan)
        