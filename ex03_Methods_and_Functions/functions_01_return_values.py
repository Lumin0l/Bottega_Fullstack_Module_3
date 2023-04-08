# How return values work with examples

def full_name(first, last): # Before we used this with 'print', only usefull for debugging in real world applications.
    return f'{first} {last}' # No '()', but delimited with ''.

kristine = full_name('Kristine', 'Hudgens') # This way we will create a variable that stores what comes after executing the full_name function.

def greeting(name):
    print(f'Hi {name}')

greeting(kristine)

# By default in python functions return 'None'.


