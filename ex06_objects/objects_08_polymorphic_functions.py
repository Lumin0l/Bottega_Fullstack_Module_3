# You have another way of doing the polymorphism thing without class inheritance, with functions.
# We will make Heading and Div into standalone classes and __init__ them.

class Heading:
    def __init__(self, content):
      self.content = content

    def render(self):
      return f'<h1>{self.content}</h1>'

class Div:
  def __init__(self, content):
    self.content = content

  def render(self):
    return f'<div>{self.content}</div>'

# Once done, we can start the function process.
# First create the vars:

div_one = Div('Some content')
heading = Heading('Some big heading')
div_two = Div('Another div')

# So we stored not only the content but the prototype of the classes.
# We haven't used render though, so we are not going to receive the shape we want:

print(div_one) # This will print the location of the var storing the class data.

# We need a function to trigger the different renders:

def html_render(name_of_tag): # We create a function that passes the name of the class as an argument and triggers the '.render' function inside it.
    print(name_of_tag.render())

html_render(div_one)
html_render(div_two)
html_render(heading)

