# You need more than 2 arguments

def greeting(*args): # This '*' represents a list or args that will be passed as imput, like in c.
    print(f'Hi ' + ' '.join(args))

greeting('Tiffany', 'Hudgens') # This is the same as before
greeting('Imanol', 'de', 'la', 'Iglesia') # This will add it all into the pointer.

# How does it work?
# It creates a tuple in memory, that is, a list that is unmutable.
# More or less the same as in C.

# It works with several arguments, but you either have to be aware of the order or name them.
def greeting_time(time, *args):
    print(f"{time} {' '.join(args)}")

greeting_time('morning', 'Imanol', 'de', 'la', 'Iglesia')

