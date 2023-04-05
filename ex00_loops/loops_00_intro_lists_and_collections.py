# How to apply loops for collections and other things:

# List
players = ['Altuve', 'Bregman', 'Correa', 'Gattis']

# Syntax is a bit wonky
for player in players: # 'players' is the name of the collection, it's fixed. 'Player' could be named anything, it's just the iterator.
    print(player)

for x in players: # this is the exact same, it's just a matter of good practices.
    print(x)
# Convention says that if the var you're iterating is a plural, we use the singular for that.


# Dictionary
players = {
  '2b': 'Altuve',
  '3b': 'Bregman',
  'ss': 'Correa',
  'dh': 'Gattis'
}

# Here we need to pick the key and the value
for position, player in players.items(): # We work with it as a view. Python will assign the values on it's own: position to keys and player to values.
    print('position:', position)
    print('player name:', player)

