# For the cases where you don't really know if you'll always have a provided arg. So it works regardless

def greeting(name = 'Guest'): # This way, if you don't pass a specific argument you'll have 'Guest'
    print(f' Hello, {name}')

greeting('Carlos')
greeting()

# Be careful. Do not assign mutable vars (like lists []) as default arguments.
# Since they are mutable, they will change in memory and carry what was assigned in the previous default call.
def some_function(collection = []):
  collection.append(1)
  print(id(collection))
  return collection

# This 2 calls will show the same memory address, but will have different values.
print(some_function()) # This will print out '[1]'
print(some_function()) # This will print out '[1, 1]', because it changed last time it was used.



