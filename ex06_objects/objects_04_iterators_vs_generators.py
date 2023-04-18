# Another option to iterate through a class, but with a generator instead of an iterator.

class Infinite_lineup:
    def __init__(self, players):
        self.players = players

    def lineup(self):
        lineup_max = len(self.players) # This will give the ammount of players
        index = 0

    # We are going to create an "infinite loop"
        while True:
            if index < lineup_max:
                yield self.players[index] # This yield keyword contains the 'next' command so we can iterate through the list.
            else:
                index = 0
                yield self.players[index]
               
    
            index += 1

    def __repr__(self):
        return f'<Infinite_lineup({self.players})'

    def __str__(self):
        return f'Infinite_lineup with the players: {self.players}'

astros = [
  'Springer',
  'Bregman',
  'Altuve',
  'Correa',                                                                                                                                                                                   
  'Reddick',                                                                                                                                                                                  
  'Gonzalez',
  'McCann',
  'Davis',
  'Tucker'
]


full_lineup = Infinite_lineup(astros)
astros_lineup = full_lineup.lineup() # We have implemented this method inside the class.

# Now we start the process of generating it:
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))


print(repr(astros_lineup))
print(str(astros_lineup))


