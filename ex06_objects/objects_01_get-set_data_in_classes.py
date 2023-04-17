# Common things in object oriented languages you have getter and setter functions.
# Python does it itself.
# We will see how to work with properties in the future.

class Invoice:

    def __init__(self, client, total):
        self.client = client
        self.total = total

    def formatter(self):
        return f'{self.client} owes: ${self.total}'

google = Invoice('Google', 100)

# now google is an object, if we wanna check atributes inside of it we can check it:
print(google.client) # this will print 'Google'

# This is a 'getter' method, a process that gets you the values inside of objects.

# Now lets go for a 'setter', a process that sets values inside objects into a different thing

google.client = 'Chrome'

print(google.client) # this will now print 'Chrome'


