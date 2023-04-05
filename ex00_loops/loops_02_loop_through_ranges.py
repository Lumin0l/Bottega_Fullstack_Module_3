# If you wanna limit the loop, you can make a range:

for num in range(1, 10): # It works pretty much like slice (start, stop). It gets 'up to stop', in our case 1 - 9. 
    print(num)

# We can also add intervals:
for number in range(1, 10, 2):
    print(number)
