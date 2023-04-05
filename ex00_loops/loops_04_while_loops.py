# Normally we'll use for in, but there is cases for while.
# For...in... is finite, it has a range and it will always stop when done. While loops do not have a fixed range, you'll have to set it yourself.
# While loops need this delimiter (sentinel value) or they can go infinite.


nums = list(range(1, 100))

# We can print them with fot.. in.. like this:
for num in nums:
    print(num)

# With while:
while len(nums) > 0: # We set the limit.
    print(nums.pop()) # We print (with .pop it will print the last element and delete it until hitting 0)

# Game for examples in which while is useful:

# Loops where you don't know the duration:
def guessing_game():
    while True: # You have no idea when it will stop exactly, so you set a semi-infinite loop. Infinite until told otherwise.
        print('What is your guess?')
        guess = input()
        
        if guess == '42': # When this if is entered the condition will turn to False and cut the loop.
            print('You win!')
            return False
        else:
            print(f'No, {guess} is not correct. Try again.\n')

guessing_game()



