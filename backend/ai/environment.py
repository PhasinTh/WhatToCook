class Environment:
    def __init__(self, globalRecipe, globalIngredient, globalPurchasable, agent, initialState, rawIngredients):
        self.globalRecipe = globalRecipe
        self.globalIngredient = globalIngredient
        self.globalPurchasable = globalPurchasable
        self.rawIngredients = rawIngredients
        self.agent = agent
        self.initialState = initialState
        self.visitedCombinations = {}

    def __Generate_Basket(self, recipe, basket, purchasedList):
        clonedBasket = basket.copy()
        for purchasedItem in purchasedList:
            if purchasedItem not in clonedBasket:
                clonedBasket[purchasedItem] =  purchasedList[purchasedItem]
            else:
                clonedBasket[purchasedItem] = clonedBasket[purchasedItem] + purchasedList[purchasedItem]
        for ingredient in recipe["ingredients"]:
            if ingredient in clonedBasket:
                clonedBasket[ingredient] = clonedBasket[ingredient] - 1
                if clonedBasket[ingredient] <= 0:
                    clonedBasket.pop(ingredient)
        return clonedBasket

    def __Generate_Purchased_Item(self, recipe, basket):
        purchaseList = {}
        for ingredient in recipe["ingredients"]:
            if ingredient not in basket:
                purchaseList[ingredient] = self.globalPurchasable[ingredient]
        return purchaseList
    
    def __Calculate_Cost(self, recipe, purchaseList):
        cost = sum([self.globalIngredient[ingredient]["cost"]*self.globalPurchasable[ingredient] for ingredient in purchaseList])
        calories = sum([self.globalIngredient[ingredient]["calories"] for ingredient in recipe["ingredients"]])
        return self.agent.caloriesPreference*calories + self.agent.costPreference*cost

    def __Is_Visited_Already(self, cookedMeal):
        clonedVisitedCombinations = self.visitedCombinations.copy()
        cookedSet = set(cookedMeal)
        if len(cookedMeal) in clonedVisitedCombinations:
            shouldAddToCombination = True
            for combinations in clonedVisitedCombinations[len(cookedMeal)]:
                if len(cookedSet.intersection(combinations)) == len(cookedMeal):
                    shouldAddToCombination = False
                    break
            if shouldAddToCombination:
                clonedVisitedCombinations[len(cookedMeal)].append(cookedSet)
                self.visitedCombinations = clonedVisitedCombinations
                return False
            return  True
        self.visitedCombinations[len(cookedMeal)] = [cookedSet]
        return False 

    def __Generate_Nodes(self, currentNode):
        for_sort_nodes = []
        if currentNode["mealNumber"] < self.agent.numberOfMeal:
            for recipe in self.globalRecipe:
                if recipe not in currentNode["cookedMeal"]:
                    selectedRecipe = self.globalRecipe[recipe]
                    cookedMeal =  currentNode["cookedMeal"] + [recipe]
                    isVisitedCombination = self.__Is_Visited_Already(cookedMeal)
                    if not isVisitedCombination:
                        purchasedList = self.__Generate_Purchased_Item(
                            selectedRecipe, 
                            currentNode["basket"]
                        )
                        basket = self.__Generate_Basket(
                            selectedRecipe, 
                            currentNode["basket"], 
                            purchasedList
                        )
                        cost = self.__Calculate_Cost(
                            selectedRecipe, 
                            purchasedList
                        )
                        heuristic = self.__Calculate_Heuristic(basket, currentNode["mealNumber"], cookedMeal)
                        if heuristic is not None:
                            for_sort_nodes.append({ 
                                "basket": basket,
                                "cost": currentNode["previousGrocceryCost"] + cost + heuristic,
                                "previousGrocceryCost": currentNode["previousGrocceryCost"] + cost,
                                "cookedMeal": cookedMeal,
                                "mealNumber": currentNode["mealNumber"] + 1,
                            })
            self.agent.fringe = self.agent.fringe + for_sort_nodes
            self.agent.fringe.sort(key = lambda x: x["cost"], reverse = False)

    def __Unrestrainded_Generate_Purchased_Item(self, recipe, basket):
        purchaseList = {}
        for ingredient in recipe["ingredients"]:
            if ingredient not in basket:
                purchaseList[ingredient] = 1
        return purchaseList

    def __Find_Cheapest_Recipe_With_Ingredient(self, ingredient, basket, cookedMeal):
        minCost = None
        cheapestRecipe = None
        cheapestPurchaseList = None
        for recipe in self.globalRecipe:
            selectedRecipe = self.globalRecipe[recipe]
            if ingredient in selectedRecipe["ingredients"] and selectedRecipe["id"] not in cookedMeal:
                purchaseList = self.__Unrestrainded_Generate_Purchased_Item(selectedRecipe, basket)
                cost = self.__Calculate_Cost(selectedRecipe, purchaseList)
                if minCost == None or cost < minCost:
                    minCost = cost
                    cheapestRecipe = recipe
                    cheapestPurchaseList = purchaseList
        if minCost == None:
            return (None, None, None)
        return (minCost, cheapestRecipe, cheapestPurchaseList)

    def __Calculate_Recipe_Cost(self, recipe):
        costList = []
        caloriesList = []
        for ingredient in recipe["ingredients"]:
            selectedIngredient = self.globalIngredient[ingredient]
            costList.append(selectedIngredient["cost"])
            caloriesList.append(selectedIngredient["calories"])
        return (self.agent.costPreference*sum(costList))+(self.agent.caloriesPreference*sum(caloriesList))

    def __Sequential_Cheapest_Recipe_Cost_For(self, cookedMeal, mealLeft):
        result = []
        for recipe in self.globalRecipe:
            selectedRecipe = self.globalRecipe[recipe]
            if selectedRecipe["id"] not in cookedMeal:
                result.append(self.__Calculate_Recipe_Cost(selectedRecipe))
        result.sort(reverse=False)
        return sum(result[:mealLeft])
        

    def __Calculate_Heuristic(self, basket, mealNumber, cookedMeal):
        clonedBasket = basket.copy()
        heuristic = 0
        counter = mealNumber + 1
        while True:
            if len(clonedBasket) == 0:
                break
            counter += 1
            if counter > self.agent.numberOfMeal:
                return None
            ingredient = list(clonedBasket.items())[0][0]
            costRecipeTuple = self.__Find_Cheapest_Recipe_With_Ingredient(ingredient, clonedBasket, cookedMeal)
            if costRecipeTuple[0] == None:
                return None
            clonedBasket = self.__Generate_Basket(self.globalRecipe[costRecipeTuple[1]], clonedBasket, costRecipeTuple[2])
            heuristic += costRecipeTuple[0]

        mealLeft = self.agent.numberOfMeal - counter
        if mealLeft != 0:
            heuristic += self.__Sequential_Cheapest_Recipe_Cost_For(cookedMeal, mealLeft)
        return heuristic

    def __To_MealPlan(self, node):
        menu = []
        basket = self.initialState["basket"]
        for recipe in node["cookedMeal"]:
            selectedRecipe = self.globalRecipe[recipe]
            purchasedList = self.__Generate_Purchased_Item(selectedRecipe, basket)
            basket =  self.__Generate_Basket(selectedRecipe, basket, purchasedList)
            ingredients = []
            for ingredient in purchasedList:
                selectedIngredient = self.rawIngredients[ingredient]
                ingredients.append({
                    "id": ingredient,
                    "name": selectedIngredient["name"],
                    "url": selectedIngredient["url"],
                    "calories": round(selectedIngredient["calories"],2),
                    "cost": round(selectedIngredient["cost"],2),
                    "quantity": round(purchasedList[ingredient],2)
                })
            menu.append(
                {
                    "id": recipe,
                    "name": selectedRecipe["recipe"],
                    "url": selectedRecipe["url"],
                    "calories": round(sum([ self.rawIngredients[ingredient]["calories"] for ingredient in selectedRecipe["ingredients"]]),2),
                    "cost": sum([ingredient["cost"] * ingredient["quantity"] for ingredient in ingredients]),
                    "shoppingList": ingredients
                }
            )
        return menu

    def Simulate(self, goalState):
        currentNode = {
            "cost": 0,
            "basket": self.initialState["basket"],
            "cookedMeal": [],
            "mealNumber": 0,
            "previousGrocceryCost": 0
        }
        self.__Generate_Nodes(currentNode)
        while len(self.agent.fringe) > 0:
            lowestCostNode = self.agent.fringe.pop(0)
            if lowestCostNode["basket"] == goalState["basket"] and lowestCostNode["mealNumber"] == goalState["numberOfMeal"]:
                return self.__To_MealPlan(lowestCostNode)
            self.__Generate_Nodes(lowestCostNode)
        return None
    
def BuildEnvironment(globalRecipe, globalIngredient, globalPurchasable, agent, initialState, rawIngredients):
    return Environment(globalRecipe, globalIngredient, globalPurchasable, agent, initialState, rawIngredients)
    
