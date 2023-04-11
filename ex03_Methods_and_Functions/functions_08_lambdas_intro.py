# Intro to lambdas
# A lambda is a type of function, or a construct. It is a tool that allows to wrap up a function and pass them to other function.
# In python functions behave like any other element, so we can wrap actions, behaviours or processes in a var to use it around inside the program.

# A lambda returns a value, so we're storing it here.
# First we declare it with 'lambda' and we write it's arguments. Then ':' and after that comes the return.

full_name = lambda first, last: f'{first} {last}' # In this case, the 'full_name' lambda takes 2 arguments and formats them into a string, that then returns.

print(full_name('Kristine', 'Hudgens')) # This will return 'Kristine Hudgens'

# We can use it to format stuff into usable things for other functions like here:
def greeting(name):
    print(f'Hi there {name}')

greeting(full_name('Tiffany', 'Hudgens'))

