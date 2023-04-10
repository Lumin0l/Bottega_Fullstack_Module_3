# How to combine all types of aargs into a single function.
# Let's create a greeting function that does it all.

def greeting(time, *args, **kwargs):
    print(f"Hi {' '.join(args)}, I hope that you're having a great {time}")

    if kwargs:
        print("Your tasks for the day are:")
        for key, value in kwargs.items():
            print(f"{key} -> {value}")


greeting('Morning',
         'Kristine', 'Hudgens', # This are going to be passed as a list, as many as you write, because they aren't preceded by the key.
         first = 'Empty dishwasher', # From here on, they will be passed as the kwargs, because they are preceded by a key.
         second = 'Take pupper out',
         third = 'math homework')

