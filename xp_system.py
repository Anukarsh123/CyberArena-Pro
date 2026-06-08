class XPSystem:

    def __init__(self):

        self.level = 1
        self.xp = 0
        self.xp_needed = 100

    def add_xp(self, amount):

        self.xp += amount

        while self.xp >= self.xp_needed:

            self.xp -= self.xp_needed

            self.level += 1

            self.xp_needed += 50
