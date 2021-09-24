import json
import numpy as np
import os

def __Find_Min_Max(objectList, key):
  min = None
  max = None
  for entry in objectList:
    currentValue = entry[key]
    if min == None or currentValue < min:
      min = currentValue
    if max == None or currentValue > max:
      max = currentValue
  return min, max
    
    
def __Normalized_Key(objectList, key, maxValue):
    clonedObjectList = objectList.copy()
    min, max = __Find_Min_Max(clonedObjectList, key)
    for entry in clonedObjectList:
      entry[key] = 1+((entry[key] - min)*(maxValue-1))/(max-min)
    return clonedObjectList
    
def __Generate_Purchaseable_List(objectList, number, max):
  purchaseableList = {}
  for entry in objectList:
    if number is None:
      purchaseableList[entry] =  int(np.random.uniform(1,max))
    else:
      purchaseableList[entry] = number
  return purchaseableList

def __Generate_Id(objectList):
    clonedObjectList = objectList.copy()
    for index, entry in enumerate(objectList):
      entry["id"] = index
    return clonedObjectList

def __Format_Ingrediet_List_To_Dictionary(ingredientList):
  ingredientDictionary = {}
  for ingredient in ingredientList:
    ingredientDictionary[ingredient["id"]] = {"name": ingredient["name"], "calories": ingredient["cal"], "cost": ingredient["cost"], "url": ingredient["picture"]}
  return ingredientDictionary

def __Find_Ingredient_Id(ingredientName, ingredientDictionary):
  for id in ingredientDictionary:
    if ingredientDictionary[id]["name"] == ingredientName:
      return id

def __Generate_Formatted_Recipes(recipeList, ingredientList):
  formattedRecipeList = recipeList.copy()
  recipeDictionary = {}
  for recipe in formattedRecipeList:
    recipe["calories"] = recipe["total_cal"]
    recipe["url"] = recipe["picture"]
    for index, ingredient in enumerate(recipe["ingredients"]):
      recipe["ingredients"][index] = __Find_Ingredient_Id(ingredient["name"], ingredientList)
    recipeDictionary[recipe["id"]]=recipe
  return recipeDictionary

def __Sample(shuffle, number, objectList):
  clonedObjectList = objectList.copy()
  if len(objectList) < number:
    return clonedObjectList
  if shuffle:
      np.random.shuffle(clonedObjectList)
  return clonedObjectList[0:number]
    

def Generate_Resources():
    recipeFile = open(os.path.join("files/recipes.json"))
    rawRecipe = json.load(recipeFile)
    ingredientFile = open(os.path.join("files/ingredients.json"))
    rawIngredients = json.load(ingredientFile)
    ingredientList = []
    ingredientList = __Normalized_Key(rawIngredients, "cost", 100)
    ingredientList = __Normalized_Key(ingredientList, "cal", 100)
    ingredientList = __Generate_Id(ingredientList)
    rawIngredients = __Generate_Id(rawIngredients)
    rawIngredients = __Format_Ingrediet_List_To_Dictionary(rawIngredients)
    ingredientList = __Format_Ingrediet_List_To_Dictionary(ingredientList)

    recipesList = []
    recipesList = __Sample(True, 50, rawRecipe)
    recipesList = __Normalized_Key(recipesList, "total_cal", 100)
    recipesList = __Normalized_Key(recipesList, "total_cost", 100)
    recipesList = __Generate_Formatted_Recipes(recipesList, ingredientList)
    purchaseableList = __Generate_Purchaseable_List(ingredientList, None,3)
    return ingredientList, recipesList, purchaseableList, rawIngredients