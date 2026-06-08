class Shop:

    def __init__(self):

        self.items = {
            "Health Potion": 100,
            "Shield": 200,
            "Laser Upgrade": 500
        }

    def buy(self, item, coins):

        if item in self.items:

            if coins >= self.items[item]:

                return True

        return False
