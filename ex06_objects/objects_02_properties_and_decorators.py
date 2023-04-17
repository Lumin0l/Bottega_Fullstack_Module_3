# The getter we have seen is considered a bad practice, because it doesn't protect the info.
# It is recommended to create methods to protect the data a processes to set other values that take the protection into account.

class Invoice:
    
    def __init__(self, client, total):
        self._client = client # an underscore before the name is a key to others that this data has to be protected.
        self.__total = total # 2 undercores mean it needs to be private

    def formatter(self):
        return f'{self.client} owes: {self.total} €'

    # To protect the stuff we use a property as a decorator:
    # Through property we stablish data as properties
    @property
    def client(self):
        return self._client

    @property
    def total(self):
        return self.__total

    # The properties take care of our getters, but we need to protect the stuff.
    # We do this by establishing specific functions for setting values with .setter
    
    @client.setter
    def client(self, client):
        self._client = client

google = Invoice('Google', 100)
print(google.client)

# Once we've established the setter, we can safely use the setting method:
google.client = 'Chrome'
print(google.client)





