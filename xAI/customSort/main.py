'''
🚨 Problem: customSort
You are given:

A string order representing a custom alphabet (e.g., "cba")

A string s you must sort using the custom order

Return a new string where characters in s are ordered according to order. Characters not in order should come after, in any order.

🧪 Example
python
Copy
Edit
Input: order = "cba", s = "abcd"
Output: "cbad"
Because 'c', 'b', and 'a' appear in order in that order, and 'd' is not in order so it comes last.

✍️ Constraints
You should preserve the frequency of letters

Assume lowercase letters

Try to write clean, real-world code — not just a one-liner
'''

def customSort(order, s):
    s_l = list(s)
    s2_l = ""

    for i in range(0, len(order)):
        for j in range(0, len(s_l)):
            if order[i] == s_l[j]:
                s2_l += s_l[j]

    for i in range(0, len(s_l)):
        if s_l[i] not in order:
            s2_l += s_l[i]

    return s2_l

print(customSort("cba", "abcd"))
print(customSort("hzyx", "xyzzyhha"))