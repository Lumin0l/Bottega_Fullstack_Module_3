# We are going to start working with the file system in python
# How we create a file and write to it:
# Like 'open', 'read' and 'write' in c

file_builder = open("logger.txt", "w+") 
# This works by opening the file that has the name passed as an argument, but if there is none it creates the file with that name.
# "w+" will allow us to write in it.

'''
The followiong line would create a file in our dir (in case there would be no "logger.txt" file) and writhe the input in it.
file_builder.write("Hey, I'm in a file!")

Then  we would need to close the file, like in c.
file_builder.close()
'''

# We can do it manually like in te comments, or we can dynamically do it with a loop or a method:

for i in range(100): # 100 and not 101, because we are doing 'i + 1' bellow.
    file_builder.write(f"I'm on line: {i + 1}\n")

file_builder.close()

# This will create 1 "logger.txt" file, because it only triggers open once, but then write 100 lines, because we trigger 'write' 100 times.
# Bear in mind it will overwrite whatever is in the file.

