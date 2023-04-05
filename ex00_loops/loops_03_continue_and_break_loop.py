# You can alter the behaviour of the loop:

usernames = [
  'jon',
  'tyrion',
  'theon',
  'cersei',
  'sansa',
]

# Let's make a loop that searches for a name and reacts different to the rest.
# For this we will use with Continue and Break:
for username in usernames:
    if username == 'cersei':
        print(f'Sorry, {username}, you are not allowed')
        continue
    else:
        print(f'{username} is allowed')
# With Contine, as if not using continue, it will keep looping after the condition is met. Shown to illustrate the difference with Break.
# Break stops the loop. I don't know what the difference with return is, I may ask.
for username in usernames:
    if username == 'cersei':
        print(f'{username} was found at index {usernames.index(username)}')
        break
    else:
        print(username)


