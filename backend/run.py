from settings import app, api
from flask_restful import Resource
from data.generator import Generate_Resources
from api.ingredients.ingredients import Ingredients
from api.mealPlans.mealPlans import MealPlan, MealPlans


ingredeintList,recipeList,purchaseableList, rawIngredients = Generate_Resources()

api.add_resource(Ingredients, "/ingredients", resource_class_kwargs={"ingredientList": rawIngredients})
api.add_resource(MealPlans, "/plans", 
resource_class_kwargs={
  "ingredientList": ingredeintList,
  "recipeList": recipeList,
  "purchaseableList": purchaseableList,
  "rawIngredients": rawIngredients
})

api.add_resource(MealPlan, "/plans/<string:id>")


if __name__ == '__main__':
    app.run(debug=True, port=8888)