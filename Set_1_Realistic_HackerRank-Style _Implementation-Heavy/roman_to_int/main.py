'''def roman_to_int(str):
    ro_in = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D": 500,
        "M":1000
    }

    s = list(str)
    total = 0

    arr = []

    for i in range(0, len(s)):
        if s[i] in ro_in:
            if i - 1 >= 0 and ro_in.get(s[i]) > ro_in.get(s[i - 1]):
                total = ro_in.get(s[i]) - ro_in.get(s[i - 1])
            else:
                print("else")
                total = total + ro_in.get(s[i])
        else:
            return "not valid roman"

    return total'''

def roman_to_int(s):
    ro_in = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    total = 0
    i = 0

    while i < len(s):
        # Look ahead to next character
        if i + 1 < len(s) and ro_in[s[i]] < ro_in[s[i + 1]]:
            total += ro_in[s[i + 1]] - ro_in[s[i]]
            i += 2  # Skip the next character
        else:
            total += ro_in[s[i]]
            i += 1

    return total

print(roman_to_int("MCM"))