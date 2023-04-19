# Pretty price exercise.
# We want to have a function that, if passed a gross value like 3.21 cents will convert it into .99, .95 or .00.

# Solution:
# pseudocode: i want to round the number and then append the suffix.
def pretty_price(raw_price, suffix):
    if isinstance(suffix, int):
        suffix = suffix * 0.01

    return int(raw_price) + suffix

print(pretty_price(3.50, 0.95))
print(pretty_price(3.50, 99))
