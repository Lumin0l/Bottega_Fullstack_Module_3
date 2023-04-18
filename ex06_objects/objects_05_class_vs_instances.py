# So far we've been using attributes when retalted to classes, with the instance attribute

class Website:
    def __init__(self,title):
        self.title = title

ws = Website('My website title')

print(ws.title)
# We can also check it with the __dict__ method
print(ws.__dict__)

# Let's create another class to differentiate the ways:

class DifferentWebsite:
    title = 'My Class Title'

dw = DifferentWebsite()
print(dw.__dict__) # This won't show anything. We didn't create an instance, we created a class attribute.

# We can access the data, but differently
print(dw.title) # The title is something that belongs to the class, hardcoded. So we need to call it to see it.

# As a summary: a 'class attribute' is inherent to the class itself. It will be present if we create a different var like 'dw_two' and assign it to it and it will be there.
# Instance attributes will only appear in every different instance.
