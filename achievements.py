class AchievementSystem:

    def __init__(self):

        self.achievements = []

    def unlock(self,name):

        if name not in self.achievements:

            self.achievements.append(name)

    def get_all(self):

        return self.achievements
