import redis
from flask import Flask
from task.celery import make_celery
from flask_restful import  Api
import json
from ai.environment import BuildEnvironment
from ai.agent import Agent

app = Flask(__name__)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response


redisConnection = redis.Redis(host="localhost", port=6379, db=0)
celery = make_celery(app)
api = Api(app)


@celery.task()
def GenerateMealPlan(taskId, caloriesPreference, costPreference, numberOfMeal, recipeList, ingredientList, purchaseableList, rawIngredients, initialState):
    agent = Agent(caloriesPreference, costPreference, numberOfMeal)
    purchaseableList =  {int(k): v for k, v in purchaseableList.items()}
    ingredientList =  {int(k): v for k, v in ingredientList.items()}
    recipeList =  {int(k): v for k, v in recipeList.items()}
    rawIngredients =  {int(k): v for k, v in rawIngredients.items()}

    environment = BuildEnvironment(
            recipeList, 
            ingredientList, 
            purchaseableList, 
            agent, 
            initialState,
            rawIngredients,
    )
    result = environment.Simulate({"basket": {},"numberOfMeal": numberOfMeal})
    if result == None:
        redisConnection.set(taskId, json.dumps({}))
    else:
        redisConnection.set(taskId, json.dumps(result))