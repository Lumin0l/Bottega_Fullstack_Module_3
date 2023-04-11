# Fizzuzz in Python with no limitations:
# Dynamic range

def Imanol_fizzbuzz(limit):
    if not isinstance(limit, int):
        print('Please, introduce an int as argument')
    else:
        for num in range(limit + 1):
            if num != 0:
                if num % 3 == 0 and num % 5 == 0:
                    print('fizzbuzz')
                elif num % 3 == 0:
                    print('fizz')
                elif num % 5 == 0:
                    print('buzz')
                else:
                    print(num)

Imanol_fizzbuzz('aasd')
print('\n')
Imanol_fizzbuzz('10')
print('\n')
Imanol_fizzbuzz(10)
print('\n')
Imanol_fizzbuzz(100)
print('\n')
# Imanol_fizzbuzz(1000)
print('\n')
# Imanol_fizzbuzz(50000)




