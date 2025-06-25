def roman_to_int(str):
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
            total = total + ro_in.get(s[i])
        else:
            return "not valid roman"

    return total

print(roman_to_int("III"))