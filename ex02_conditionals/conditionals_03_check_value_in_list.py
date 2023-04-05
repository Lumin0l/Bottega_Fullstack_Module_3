# We use the 'in' operator
sentence = 'The quick brown fox jumped over the lazy dog'
word = 'quick'

if word in sentence:
    print('we found it')
else:
    print('we did not find it')

# It is case sensitive
word_2 = 'Fox'
if word_2 in sentence:
    print('found it')
else:
    print('not found')

# We can also use it in lists. in dicts...


