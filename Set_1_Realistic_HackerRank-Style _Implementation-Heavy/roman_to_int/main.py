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

print(roman_to_int("IIII"))

'''
Main Take Aways: 
- my_dict = {"A": 1, "B": 2}

# This will crash
print(my_dict["C"])  # KeyError

# This will return None
print(my_dict.get("C"))  # None

# This will return -1 as default
print(my_dict.get("C", -1))  # -1
💡 When to Use Which:
Use ro_in[s[i]] when you are sure the key exists.

Use ro_in.get(s[i]) if the key might be missing, and you want to avoid a crash.

- ❌ "IIII" is not a valid Roman numeral by classical Roman rules.
✅ Why It’s Sometimes Allowed in Code:
Many coding problems do not validate strict Roman formatting. They only:

Convert based on symbol values (e.g., I = 1, so IIII = 4)

Allow leniency for ease of parsing

But in real-world or historical use, IIII would be considered invalid.

- When performing a running total and you want to do additional calculations next 
to just total += total, those calculations are treated as if they are in parenthesis. 
As a result, if you want to keep a correct running total, you will need to skip some 
elements so they dont get recalculated
'''