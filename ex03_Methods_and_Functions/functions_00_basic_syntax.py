# Examples of python functions.

# Example 1: function that provides a name.

def full_name(first, last): # So, first 'def' -> then name of the function -> then arguments (no need for type) -> then colon ':'.
    print(f'{first} {last}') # Then comes the indentation, at least 2 space.


# By convention you leave 2 enters after the end of a function.
full_name('Imanol', 'de la Iglesia')


# Example 2: authentication
def auth(email, password):
    if email == 'idelaiglesia@gmail.com' and password == 'mycoolpass':
        print('authorized')
    else:
        print('not authorized')


auth('idelaiglesia@gmail.com', 'mycoolpass')
auth('pasdaf@gmail.com', 'mycoolpass')


# Functions with no argments:
def hundred(): # No need for 'void'
    for num in range(1, 101):
        print(num)



hundred()    
