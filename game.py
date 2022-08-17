import random

class Game:
    points = 0

    def get_points(self):
        return Game.points

    def guess_the_number(self, user_number):
        self.random_number = random.randint(1, 6)
        if self.random_number == user_number:
            Game.points += 1
            return True
        return False

