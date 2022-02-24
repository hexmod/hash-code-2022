class Project:

    def __init__(self, numRoles, daysToComplete, score, bestBefore):
        self.numRoles = numRoles
        self.daysToComplete = daysToComplete
        self.score = score
        self.bestBefore = bestBefore
        self.roles = {}

    def add_role(self, name, reqLevel):
        self.roles[name] = reqLevel