class Project:

    def __init__(self, name, daysToComplete, score, bestBefore, numRoles):
        self.name = name
        self.numRoles = numRoles
        self.daysToComplete = daysToComplete
        self.score = score
        self.bestBefore = bestBefore
        self.roles = {}
        self.orderedRoles = []

    def add_role(self, name, reqLevel):
        self.roles[name] = reqLevel
        self.orderedRoles.append(name)

    def print(self):
        print(self.name, self.roles)