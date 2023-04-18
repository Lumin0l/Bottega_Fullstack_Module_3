# Introduction to constructor functions.

# It's done with the '__init__' keyword.

class Invoice:
    def __init__(self, client, total): # When you create the invoice keyword it will first come to the __init__ function and initialize everything in it.
        
        # Most things in python are objects, so what we want to do first is order the imput into the self object, so it can be usable through the rest of the class. As I understand so far.
        # So, we create 2 var that are directly linked to the 'self' instance.
        self.client = client
        self.total = total

    # So, now we create the format in which the data we structure through this class will be returned.
    def formatter(self):
        return f'{self.client} owes: {self.total} €'


# Now let's test it, let's create two instances for this class:
google = Invoice('Google', 100) # -> We state that the client google owes us 100 €.
snapchat = Invoice('SnapChat', 200)


# Let's see what it returns raw:
print(f'raw: {google}')
print(f'raw: {snapchat}')
# So, if no inner function with a return value is specified, it will return the memmory location of the class.

print(google.formatter())
print(snapchat.formatter())

# CONTINUATION #

# Python doesn't have private/protected methods. You need to do it with Dunder (__xx__) methods.
# Dunder methods are methods given from the python language and you can use it as is intended.

# Let's explain Dunder String:
print('\nNew Lesson\n')

class Invoice:
    def __str__(self):
        return 'This is the invoiceclass!'

inv = Invoice() # The __str__ method checks out the content of a class as a string
print(str(inv))

class Invoice:
    def __init__(self, client, total):
        self.client = client
        self.total = total

    def __str__(self):
        return f'Invoice from {self.client} for {self.total} dollars'

inv = Invoice('Google', 500) # We normally create the str function to receive visual feedback on the class.
print(str(inv)) # By creating the __str__ method, we can call it whenever we want to see  or debug.





