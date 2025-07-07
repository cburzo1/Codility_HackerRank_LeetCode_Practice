'''def fizzBuzz(n):
    arr_str = []

    i = 1
    while i <= n:
        if i % 3 == 0:
            arr_str.append("Fizz")
        elif i % 5 == 0:
            arr_str.append("Buzz")
        else:
            arr_str.append(str(i))

        if i % 3 == 0 and i % 5 == 0:
            arr_str[i - 1] = "FizzBuzz"

        i += 1

    print(arr_str)

    return arr_str

fizzBuzz(5)'''

def fizzBuzz(self, n):
    arr_str = []

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            arr_str.append("FizzBuzz")
        elif i % 3 == 0:
            arr_str.append("Fizz")
        elif i % 5 == 0:
            arr_str.append("Buzz")
        else:
            arr_str.append(str(i))

    return arr_str

'''
Main Take Aways: 
- Mastery of the Modulus Operator %
It's used to detect multiples, even/odd, cycles, and boundary resets.

This is a common pattern in:

Scheduling (e.g., every 7th day)

Hashing (e.g., index = hash % array_size)

Pattern repetition problems (e.g., "every k-th element")

- Loop Boundaries and Off-by-One Errors
Choosing while i <= n (or for i in range(1, n + 1)) vs i < n is a classic bug source.

Especially important in:

Time-based problems (e.g., timestamps)

Matrix traversal

String and array slicing
'''