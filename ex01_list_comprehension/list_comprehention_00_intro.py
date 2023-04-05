# Intro to list comprehension
# We can generate lists from loops
# Mix of for..in.. loops and conditionals inside a single line of code.

# Lets make a list that cubes numbers
num_list = range(1, 11) # this will give 1 - 10
cubed_nums = []

# Wihtout list comprehension we have to do this:
for num in num_list:
    cubed_nums.append(num ** 3)

print(cubed_nums)

# With list comprehension:
# We dynamically allocate the list:
cubed_nums = [num ** 3 for num in num_list]

print(cubed_nums)

# Let's explain:
# We hace: ['the action we want done to what var' FOR 'the var' IN 'the list that gets iterated']

# We have yet more options:
# Let's say we want a list that only gets the even numbers:

# Base case:
even_numbers = []

for num in num_list:
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers)

# With list comprehension
even_numbers = [num for num in num_list if num % 2 == 0]
print(even_numbers)

# What is going on?
# ['return var' FOR 'var' IN 'list where var is' IF condition]
