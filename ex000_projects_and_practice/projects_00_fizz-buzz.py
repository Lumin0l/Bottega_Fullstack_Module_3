# Fizzuzz in Python with no limitations:
# Dynamic range

"""
Write a program that prints the numbers from 1 to 100.
But for multiples of three print “Fizz” instead of the
number and for the multiples of five print “Buzz”. For
numbers which are multiples of both three and five print
“FizzBuzz”.
"""

def Imanol_fizzbuzz(limit):
    if not isinstance(limit, int):
        print('Please, introduce an int as argument')
    else:
        for num in range(limit + 1):
            if num != 0:
                if num % 3 == 0 and num % 5 == 0:
                    print('fizzbuzz')
                elif num % 3 == 0:
                    print('fizz')
                elif num % 5 == 0:
                    print('buzz')
                else:
                    print(num)

Imanol_fizzbuzz('aasd')
print('\n')
Imanol_fizzbuzz('10')
print('\n')
Imanol_fizzbuzz(10)
print('\n')
Imanol_fizzbuzz(100)
print('\n')
# Imanol_fizzbuzz(1000)
print('\n')
# Imanol_fizzbuzz(50000)

# Their solution:

def fizz_buzz(max_num):
  for num in range(1, max_num + 1):
    if num % 3 == 0 and num % 5 == 0:
      print('FizzBuzz')
    elif num % 5 == 0:
      print('Buzz')
    elif num % 3 == 0:
      print('Fizz')
    else:
      print(num)

fizz_buzz(100)

# I like mine better because it deals with wrong argument types, but I like how they use 'range' better.
# I didn't know there was a way to set '1' as the starting point, so I had to make an if statement to ignore the '0'. Now I know.


