# Can you also give named args in a list?

def greeting(**kwargs): # kw is the convention for KeyWord. It is kind of like a double pointer in C, but it refers to a dictionary: '*' -> key, '*' -> words.
    print(kwargs)

greeting(first = 'Imanol', second = 'de la Iglesia Muriel') # the first element will be the key and the second will be the content.

# LEt's see it in use:

def greeting_two(**kwargs):
    if kwargs:
        print(f"Hi {kwargs['first']} {kwargs['second']}, have a nice day!")
    else:
        print('Hi Guest, have a nice day!')

greeting_two(first = 'Imanol', second = 'de la Iglesia Muriel') 
greeting_two()


