# They allow if-else operations.
# You have to be careful, because they can be very easily missused.
# Most of the times they make the code harder to read too.

# Let's create a limit for admin access into accounts:
role = 'admin' # can be guest, student...

auth = 'can access' if role == 'admin' else 'cannot access' # we'll store the result of our ternary operatos

# In normal terms:
if role == 'admin':
    auth = 'can access'
else:
    auth = 'cannot access'

# Ternary operators allow only 1 assignment, so they are shorter. Problem is they can get complicated veery fast.



