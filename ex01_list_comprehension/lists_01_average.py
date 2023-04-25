# How to get the average from a list:
# Let's show some libs that do that first:
'''
import statistics
print(statistics.mean(list)

That will give the average using the statistics list in a very thorough way

import numpy
print(numpy.mean(list)

Also this

functools too.
'''

# My attempt at doing it without libs:

num_list = [1, 2, 3, 4, 5, 6]

def total_sum(num_list):
    result = 0
    total = 0
    for num in num_list:
        result += num
    total = result / len(num_list)
    return total

print(f'My total: {total_sum(num_list)}')


# His solution

from functools import reduce # yes, the dude says "let's do it with no libraries" and then imports a library...

def get_average(num_list):
    total = reduce((lambda total, element: total + element), num_list)
    return total / len(num_list)

print(f'His total: {get_average(num_list)}')
