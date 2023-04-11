# We need to make a program to retrieve the titles to the links from the daily smary python webpage.

# First we import the libraries
import requests # To make the HTTP requests and get the raw HTML.
from bs4 import BeautifulSoup # To parse the raw HTML and extract the links.
import inflection # To transform the text we extract and turn it into the required format.

# We retrieve the HTML from the webpage using '.get()' as we saw before:
# This will make a HTTP GET request from the webpage and retrieve the information as a "Response Object" in raw bytes.

response_object = requests.get('http://www.dailysmarty.com/topics/python')

# Then, we need to clean this data into usable material.

# The response object has an attribute called 'content' that contains the raw HTML, so with '.content' we store what layis within the attribute into a variable.

raw_html = response_object.content

# Note: the data stored in .content is in bytes, we can't use it as is.
# ChatGPT retrieves the info with .content because we will later pass it to BeatifulSoup, but we could also use '.text' to retrieve it as a decoded string.

# Now we will parse that raw_html into a 'BeautifulSoup Object' so it becomes usable:

# BeatifulSoup is a constructor that creates said special object.
# It takes 2 arguments: the content we want to parse in bytes (raw_html) and the parser we want to use to process it, in out case 'html.parser' included in Python.
# When doing this, a new object will be created containing all this info in a tree like representation so we can navigate it easily.

soup = BeautifulSoup(raw_html, 'html.parser')

# Now we will extract the links from that clean beautifulsoup object:

# We will use the 'find_all()' method to extract the links with the post-link class.

post_links = soup.find_all('div', {'class': 'post-link-title'})

# Now we clean the post titles using the inflection library:

# From the inflection library we use titleize and .strip() to strip the titles.

for link in post_links:
    post_title = inflection.titleize(link.text.strip())
    print(post_title)
