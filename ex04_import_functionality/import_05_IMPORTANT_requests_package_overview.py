# The request package is used to communicate with APIs
# API means 'Application Programming Interface". It is a language for our application to use and communicate with third party apps.

# We are going to communicate with 'DailySmarty' by going to api.DailySmarty.com/posts
# It's in JSON: 'JavaScript Object Notation'. It is similar to the dictionaries in python in the sense that they work in key-value pairs.
# It is a structured way to organize the data so other apps will be able to connect with it.

'''
To use request, first we need to install it:
    - pip install requests
After that we can start using it.

'''

# Let's start the example:
import requests
import pprint

r = requests.get('https://api.dailysmarty.com/posts') # This will use the function get to go to the webpage and get the API.
r.json() # If we print this it will be terrible, because it will be printed with no format.

# Lets use pretty print:
pprint.pprint(r.json())

# Woohoo! first time using APIs, this is going to be a constant from now on.

# Now let's use what we got. Let's filter the posts
pprint.pprint(r.json()['posts'][0]['url_for_post'])
'''
Explanation of what happened:


    - pprint.pprint: This is a function from the pprint module that pretty-prints the output to the console in a nicely formatted way. It takes an object as an argument and prints it to the console.

    - r.json(): This is a method that parses the JSON content of an HTTP response object r and returns it as a Python object. In this case, it returns a dictionary object.

    - ['posts'][0]: This accesses the first element in the posts list of the returned dictionary object.

    - ['url_for_post']: This accesses the value of the url_for_post key in the first element of the posts list.

So, when you put all these parts together, the full line of code prints out the value of the url_for_post key in the first element of the posts list of a JSON response received from an API endpoint, in a nicely formatted way using the pprint function.
'''
