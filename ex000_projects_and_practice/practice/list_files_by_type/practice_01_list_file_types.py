# Just sort stuff by type '.txt, .c, .py...'
# Before this we will create several files of different types

# First we import 2 libraries:
import fnmatch # Built into python
from fnmatch import fnmatchcase
import os # Built into python, gives access to operating system

def list_files():
    for file in os.listdir('.'): # os.listdir() function gives access to a directory and we add the path.
        if fnmatch.fnmatch(file, "*.txt"): # The lib is called like that, but also the main function we want.
            print("Text files: ", file)

        if fnmatch.fnmatch(file, "*.rb"):
                print("Ruby files: ", file)

        if fnmatch.fnmatch(file, "*yml"):
                print("Yaml file: ", file)

list_files()

players = [
    "Jose Altuve 2B",
    "Carlos Correa SS",
    "Alex Bregman 3B",
    "Scooter Gennett 2B"
]

second_base_players = [player for player in players if fnmatchcase(player, "* 2B")]

print(second_base_players)

