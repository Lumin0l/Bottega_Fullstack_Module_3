# How to allow nested functions, not present in many languages (but present in C)
# We have our previous stuff. But we can make it more efficient:
def full_name(first, last):
    return f'{first} {last}'

Kristine = full_name('Kristine', 'Hudgens')

def greeting(name):
  print(f'Hi {name}!')


greeting(Kristine)

# Example:
def greeting_2(first, last): # The parent function takes the arguments
    def full_name():
        return f'{first} {last}'
    print(f'hi {full_name()}') # Since the function has a return value it can be inside a formated string.

greeting_2('Kristine', 'Marteen')



