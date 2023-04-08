# Untill now we've seen how the args are passed in order (first, second) -> (kristine, hudgens) = 'kristine hudgens'.
# In larger programs, having possitional args can be problematic, mostly when a function calls another and so on.

# You can name the args by litterally naming them:
def full_name(first, second):
    print(f'{first} {second}')

full_name(second = 'Hudgens', first = 'Kristine')



