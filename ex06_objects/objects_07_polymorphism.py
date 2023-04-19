# Inheritance is normally used for polymorphism, create different versions of the same thing. 
# Let's create an html class and then build multiple classes to make different versions of these classes.

class Html:
    def __init__(self, content):
        self.content = content

    def rendr(self):
        raise NotImplementedError('Subclass must implement render method') 
        # I have never seen 'raise' or the other thing before. It is used to create an 'abstract class', meant not to be used by the user. It will contain methods and rules.

class Heading(Html):
    def render(self):
        return f'<h1>{self.content}</h1>'

class Div(Html):
    def render(self):
        return f'<div>{self.content}</div>'

# Let's generate the content now:

# first a list with the data:
tags = [
        Div('Some content'),
        Heading('Some big heading'),
        Div('Another div')
        ]

for tag in tags:
    print(tag.render())





