'''
In this section we'll learn how to access very powerful outside libraries.

Lets first review how to call a library from the core.

Some usefull functions are integrated into the core python system, but for efficiency reasons need to be specifically imported when used.
We can import stuff by typing "import" and the name of the library such as:
    import math

Now, how we make custom libraries (like the '.h' for C).

We create it like this:
    - create a python file (this very one).
    - add the functions we want.
    - save it.
    - import + name_of_the_file.

To use functions inside the imported library we do it like this:
    Let's say the file is called "helper" and that we have a function called "greeting" that takes 2 arguments.
    - import helper
    - helper.greeting(one, two)
    And done.

'''
