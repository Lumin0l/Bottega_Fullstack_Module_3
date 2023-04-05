# How to mix lists

legacy_customers = ['Alice', 'Bob']
new_customers = ['Tiffany', 'Kristine']

# If we mix the list as is we have this options:
raw_list = [legacy_customers, new_customers] # But this will be wrong, it will give embeded lists.
raw_list_two = legacy_customers + new_customers # This would work, but we can be more granular with loops.
print(raw_list_two)

# With loops:
for legacy_customer in legacy_customers:
    new_customers.append(legacy_customer) # This will add to the end. We can use it recursively.

print(new_customers)


