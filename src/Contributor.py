class Contributor:

    def __init__(self, name, numSkills):
        self.name = name
        self.numSkills = numSkills
        self.skills = {}

    def has_skill_for_role(self, aRole, required_skill)
        return self.skills[aRole] >= required_skill

    def add_skill(self, name, level):
        self.skills[name] = level

    def update_skill(self, name, levelWorkedAt):
        if levelWorkedAt == self.skills[name] or levelWorkedAt == self.skills[name] + 1:
            self.skills[name] = self.skills[name] + 1

    def print(self):
        print(self.name, self.skills)

    def get_skill_level(self, skill):
        if skill in self.skills:
            return self.skills[skill]
        else:
            return 0

    def get_name(self):
        return self.name