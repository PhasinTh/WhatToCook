class Agent:
    def __init__(self, caloriesPreference, costPreference, numberOfMeal):
        self.fringe = []
        self.caloriesPreference = caloriesPreference
        self.costPreference = costPreference
        self.numberOfMeal = numberOfMeal