# Loops that go through the content of a class.

# Let's say we have a list of players that we want to iterate through:
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

# In a traditional scoreboard, we would like to go through the last element and automatically go back to the first, regardless of how many elements there are.
# For this we create a class:

class Lineup:
    def __init__(self, players):
        self.players = players

    # To iterate stuff in the class, we need to enbed the methods:
    
    def __iter__(self): # This will allow us to iterate.
        self.n = 0 # we define where we are in the lineup
        return self

    def __next__(self): # This, once the __iter__ is implemented, will allow us to go to the next item.
        if self.n < (len(self.players) - 1): # so, if the index is not the last one (len -1 because we start at '0'), do this:
            player = self.players[self.n]
            self.n += 1
            return player
        else:
            player = self.players[self.n]
            self.n = 0
            return player

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

astros_lineup = Lineup(astros)
process = iter(astros_lineup)

print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))


# REFACTORING #
print('\nRefactoring\n')

class Lineup:

    def __init__(self, players):
        self.players = players
        self.last_player_index = (len(self.players) - 1) # we'll create a new instance for this line that got repeated. So it will store the enxt player.

    def __iter__(self):
        self.n = 0
        return self

    def get_player(self, n): # we also had duplicate code when getting the player, so let's create another function that simply returns the 'n'th player.
        return self.players[n]

    def __next__(self):
        if self.n < self.last_player_index:
            player = self.get_player(self.n)
            self.n += 1
            return player
        else:
            player = self.get_player(self.n)
            self.n = 0
            return player
astros_lineup = Lineup(astros)
process = iter(astros_lineup)

print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))

