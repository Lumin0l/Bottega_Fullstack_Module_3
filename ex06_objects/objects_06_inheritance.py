# The ability to create specialized versions of classes.

class User:
    def __init__(self, email, first_name, last_name):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def greeting(self):
        return f'Hi {self.first_name} {self.last_name}'


# An example of inheritance could be used when building classes that are related to other classes.
# A good example would be 'admin users' being a type of 'user'.
# We have the class 'user' but then we can become more specific and create AdminUser:

class AdminUser(User): # Since it's a tipe of user, we just use the class as an argument.
    def active_users(self): # Let's create a function that returns the ammount of active users so it's not empty.
        return '500'

# LEt's test it out:

# Admin User: will need all the imput that the regular class has
tiffany = AdminUser('tiffany@gmail.com', 'Tiffany', 'Hudgens')

# Normal user:
kristine = User('kristine@gmail.com', 'Kristine', 'Hudgens')

# Let's make some calls now to see the behaviour:

# We can call 'active users' for tiffany, since that is the function we added in the new class.
print(tiffany.active_users())
# But if we try to do it with kristine, it will crash, because in the original class there was no 'active users' function.

# On the other hand, we can call 'greeting' on tiffany, because it inherited that function from the original class:
print(tiffany.greeting())



