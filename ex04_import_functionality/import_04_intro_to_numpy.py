'''
There is a list of the libraries in Pypi.python.org

'numpy' is one of the most popular libraries. It allows to process very large numbers of data.

To install it we use 'pip' and it will serve as an example to how to install any package.

We type:
    - pip install numpy

'''

# Let's see examples for numpy
# Example: we have a list like this: [1, 2, 3, 4, 5, 6, 7, 8] and we want an embeded list with pairs like this: [[1, 2], [3, 4]...]

import numpy as np # we will alias it to make things easier.

num_range = np.arange(16) # this function creates an array of the range we type.
print(num_range)

num_range_matrix = num_range.reshape(4, 4) # this creates matrixes of the given values, in our case 4x4.
print(num_range_matrix)

# Okay, the guide doesn't explain how to complete the example it sets xD let's try ourselves:
# After checking info, this is how it's done:

starter_list = [1, 2, 3, 4, 5, 6, 7, 8]

# We need to convert that list into a numpy array, a special type of object in the lib.
np_array = np.array(starter_list)

# We use reshape to create these matrixes, but only with 2 columns and as many rows as we need.
reshaped_np_array = np.reshape(np_array, (-1, 2)) # As an extra, the '-1' assigns number of rows automatically based on the number of collumns. We could have used '1' in our case too.

# This will still be a numpy array, we need to turn it back into a list.
finished_list = reshaped_np_array.tolist()

print(finished_list)
