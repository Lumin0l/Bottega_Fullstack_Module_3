# Multiple conditions inside a python program.
# And / Or

username = 'jon'
email = 'jon@gmail.com'
password = 'thenorth'

if username == 'jon' and password == 'thenorth':
    print('Access permitted')
else:
    print('not you')

# In an uglier way, but works the same, you can do nested 'ifs'
if username == 'jon':
    if password == 'thenorth':
        print('Access permitted')
else:
    print('no')

# Use Or
if username == 'jon' or password == 'thenorth':
    print('Access permitted')
else:
    print('no')

# We can chain more than 2 conditions:
if (username == 'jon' or email == 'jon@gmail.com') and password == 'thenorth':
    print('Access permitted')
else:
    print('no')

# Sometimes you wanna check when things are or are not true
logged_in = True
standard_user = True

if logged_in and not standard_user: # So, the first has to be true AND the second has to be false.
    print('Access permitted')
else:
    print('You can only access standard sections')
