import os
from flask_restful import Resource
import numpy as np
class Ingredients(Resource):

    def __init__ (self, **kwargs):
        self.ingredientList = kwargs["ingredientList"]

    def get(self):
        numberOfIngredient =  np.random.randint(1,high=5, size=1)
        randomIngredient = np.random.randint(1, high=len(self.ingredientList), size=numberOfIngredient[0])
        ingredient = []
        for random in randomIngredient:
            selectedIngredient = self.ingredientList[random]
            ingredient.append({
                "id": int(random),
                "name": selectedIngredient["name"],
                "quantity": int(np.random.randint(1, high=3, size=1)[0]),
                "url": selectedIngredient["url"],
                "cost": round(selectedIngredient["cost"],2),
                "calories": round(selectedIngredient["calories"],2),
            })
        return {"ingredients": ingredient}
        
        