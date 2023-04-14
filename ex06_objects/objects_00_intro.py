# Intro to object classes, what are they and what is the syntax:
# We're going to do it through real world type examples:

# We start with classes.
# Classes are object mappers, they allow us to define behaviours.
class Invoice:
    
    def greeting(self): # Inside the class, you need to declare the instance when it's called, so by setting 'self' it will take it when instantiated.
        return 'Hi there'

# For now we will leave it like this. We create the blueprint done and in case we wanna use it we need to use 'instantiation'
# Let's create an object using this blueprint

inv_one = Invoice()
print(inv_one) # This will show the instances, the location in memmory where this object is stored.

# How do we call the greeting function stored inside our class?
print(inv_one.greeting())

# Sound familiar? This is how we have been using many libraries and specialized functions.


