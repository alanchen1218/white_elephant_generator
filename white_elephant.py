import random
import collections

# print(random.randint(0, 5))

class WhiteElephantGenerator:
    def __init__(self):
        self.number_of_players = -1
        self.player_list = []
        self.random_numbers = []
        self.unordered_randomize_list = {}

    def check_how_many_people(self):
        self.number_of_players = int(input("Enter how many people are playing: "))
        print("There are " + str(self.number_of_players) + " people playing the game.")
    
    def get_players(self):
        for i in range(1, self.number_of_players + 1):
            player = input("Enter player's name: ")
            self.player_list.append(str(player))
        print("Players:", self.player_list)

    def random_list(self):
        while len(self.random_numbers) < self.number_of_players:
            number = random.randint(1, self.number_of_players)
            if number in self.random_numbers:
                continue
            else:
                self.random_numbers.append(number)
        print("Order:", self.random_numbers)
    
    def create_randomized_list(self):
        self.unordered_randomize_list = dict(zip(self.random_numbers, self.player_list))
    
    def display_order(self):
        ordered_dict = collections.OrderedDict(sorted(self.unordered_randomize_list.items()))
        for key, value in ordered_dict.items():
            print(key, value)

if __name__ == '__main__':
    start = WhiteElephantGenerator()
    start.check_how_many_people()
    start.get_players()
    start.random_list()
    start.create_randomized_list()
    start.display_order()
