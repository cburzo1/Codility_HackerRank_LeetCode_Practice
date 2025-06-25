'''def add_digits(num):

    s = str(num)
    s2 = list(s)
    total = 0

    if len(s) == 1:
        return num

    while len(s) > 1:
        s = str(num)
        s2 = list(s)
        total = 0
        for i in range(0, len(s2)):
            total = total + int(s2[i])
            num = total

    s = str(num)
    s2 = list(s)
    total = 0

    if len(s) > 1:
        for i in range(0, len(s2)):
            total = total + int(s2[i])
            num = total

    s = str(num)
    s2 = list(s)
    total = 0

    if len(s) > 1:
        for i in range(0, len(s2)):
            total = total + int(s2[i])
            num = total

    return total'''

def add_digits(num):
    s = str(num)

    if len(s) == 1:
        return num

    while len(s) > 1:
        s2 = list(s)
        total = 0
        for i in range(0, len(s2)):
            total = total + int(s2[i])

        num = total
        s = str(num)

    return num

print(add_digits(49))
print(add_digits(0))
print(add_digits(7))

'''
Main Take Aways: 
- Counting digits by casting a number to a string then an iterable list
- Iterating until a fixed condition is met, often called fixed-point iteration.
- running totals
'''