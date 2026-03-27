class game:
    def __init__(self, name="", year=0, multiplayer=0, note=0):
        self.name = name
        self.year = year
        self.multiplayer = multiplayer
        self.note = note

    def __str__(self):
        return f"Game: {self.name}"



game1 = game("skyrim", 2013, True, 9.5)
print(game1)


# game1 = game()
# game1.name_game = 'gta'
# print(game1)
# first game

# game1 = game()
# game1.name_game = 'skyrim'
# game1.year_launch = 2013
# game1.multiplayer = True
# game1.note = 9.5
# print(f"o nome do jogo: {game1.name_game}, lançado em {game1.year_launch}")