# Their solution to the web scrapper exercise:

# The imports
import requests
from bs4 import BeautifulSoup # bs4 stands fot 'beautifulsoup4', which is the current version.
from inflection import titleize

# Definitions:
def titles_generator(links): # This function will take the links and store them in a list we can manipulate.
    titles = []
    
    def post_formatter(url): # This nested function will filter out what gets stored (the titles in our case)
        if 'posts' in url:
            url = url.split('/')[-1] # split every time there is a '/' into a list. Now, we only want the title, which is the last element, so we write '[-1]' for us to keep the las el.
            url = url.replace('-', ' ') # easy. We wanna replace all '-'s with ' 's.
            url = titleize(url) # we can call it as is because it's the only function we're importing, according to the teacher. Check further.
            titles.append(url)
    
    # The code has been updated in the notes, here's the patches:
    for link in links:
        if link.get('href') == None:
            continue
        else:
            post_formatter(link.get("href"))
        
    return titles


# Now the request
r = requests.get('http://www.dailysmarty.com/topics/python')

# Now we turn it into soup
soup = BeautifulSoup(r.text, 'html.parser') # See, the teacher does it with '.text' instead of '.content' so he can use it.

# Now the links
links = soup.find_all('a') # This will find all the links, because that is the tag in html. We will get all links, even the ones we don't want.

# Filter the titles with a function:
titles = titles_generator(links)

for title in titles:
    print(title)
