class Project:

    def __init__(self, name, daysToComplete, score, bestBefore, numRoles):
        self.name = name
        self.numRoles = numRoles
        self.daysToComplete = daysToComplete
        self.score = score
        self.bestBefore = bestBefore
        self.roles = [] # tuple (role, reqSkill) in order
        self.assignedRoles = {} # num -> contributor

    def add_role(self, name, reqLevel):
        self.roles.append((name, reqLevel))

    def print(self):
        print(self.name, self.roles)

    def add_contributor(self, contributor, roleIndex):
        self.assignedRoles[roleIndex] = contributor

    def is_contributor_assigned(self, contributor):
        return contributor in self.assignedRoles.values()

    def get_roles(self):
        return map(lambda x: x[0], self.roles)

    def get_skill_for_role(self, roleIndex):
        return self.roles[roleIndex][1]

    def is_completed(self):
        return len(self.roles) == len(self.assignedRoles)

    def get_name(self):
        return self.name

    def get_ordered_roles(self):
        res = ""
        for contributor in self.assignedRoles.values():
            res += contributor.get_name()
            res += " "
        return res[:-1]

    def train_contributors(self):
        count = 0
        for role, skill in self.roles:
            self.assignedRoles[count].update_skill(role, skill)
            count += 1

    def get_shortest_completion_difference(self):
        if self.bestBefore - self.daysToComplete < 0:
            return 99999999999999999999999999999
        return self.bestBefore - self.daysToComplete