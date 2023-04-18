# __str__ is meant to give some pretty, formatted output. 
# __repr__ is also used to get output from the class for debugging and so on, but it's more raw. Normally goes into the logs.

class Invoice:
  def __init__(self, client, total):
    self.client = client
    self.total = total

  def __str__(self):
    return f"Invoice from {self.client} for {self.total}"

  def __repr__(self):
    return f'Invoice <value: client: {self.client}, total: {self.total}>'

inv = Invoice('Google', 500)
# They have the same purpose:
print(str(inv)) # str is done for a more pretty representation.
print(repr(inv)) # repr is done for a more raw representation of the data itself.


