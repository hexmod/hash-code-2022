class Project:

    def __init__(self, name, daysToComplete, score, bestBefore, numRoles):
        self.name = name
        self.numRoles = numRoles
        self.daysToComplete = daysToComplete
        self.score = score
        self.bestBefore = bestBefore
        self.roles = {}
        self.orderedRoles = []
        self.assignedRoles = {}

    def add_role(self, name, reqLevel):
        self.roles[name] = reqLevel
        self.orderedRoles.append(name)

    def print(self):
        print(self.name, self.roles)

    def add_contributor(self, name, role):
        self.assignedRoles[role] = name

    def is_contributor_assigned(self, name):
        return name in self.assignedRoles.values()

    def get_roles(self):
        return self.roles

    def get_skill_for_role(self, role):
        return self.roles[role]

    def is_completed(self):
        return len(self.roles) == len(self.assignedRoles)

    def get_name(self):
        return self.name

    def get_ordered_roles(self):
        res = ""
        for aRole in self.roles:
            res += self.assignedRoles[aRole]
            res += " "
        return res[:-1]