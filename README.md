# WhatToCook

## Models

### Ingredient
```
{
 "id": Number,
 "name": String,
 "url": String,
 "calories": Number,
 "cost": Number,
 "quantity": Number
}
```

### Menu
```
{
 "id": Number,
 "name": String,
 "url": String,
 "calories": Number,
 "cost": Number,
 "shoppingList: Ingredient[]
}
```



### Plans
```
 {
  "id": Number
  "menu": Menu[]
 }
```

### PlanRequest
```
{
 "numberOfMeal": Number,
 "ingredients": Map<Number,Number>
 "caloriesPreference": Float,
 "costPreference": Float,
 }
```

## API
| URL      | HTTP ACTION | Request Payload | Response Payload| DESCRIPTION |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| /ingredients| GET |  | ```"{ ingredients: Ingredient[] } ```| Get a random amount of ingredients |
| /plan   | POST |```{ "planRequest": PleanRequest } ``` | ```{ "id": Number } ```| Create a plan request, the system will return a Plans's id |
| /plan/{planId} | GET | |```{ "plan": Plan} ```| Return a plan with the id of  ``` planId ``` if its status is completed, and empty plan indicate that it is not possible to generate a plan from such ingredients settin |
