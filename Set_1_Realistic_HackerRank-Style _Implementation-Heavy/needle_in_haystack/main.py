'''
🔧 Problem: Implement strStr()
(aka "Needle in a Haystack")

Prompt:
Implement strStr(haystack: str, needle: str) -> int, which returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack. If needle is an empty string, return 0.

✅ Constraints:
0 <= haystack.length, needle.length <= 10^4

All input characters are lowercase English letters.

You may not use .find() or similar built-in search functions.
'''

'''
MY ATTEMPT:
def needle_in_haystack(haystack ,needle):
    h_s_l = list(haystack)
    n_s_l = list(needle)

    if needle == "":
        return 0

    i = 0
    j = 0
    s = ""

    while i < len(h_s_l):
        if h_s_l[i] == n_s_l[j]:
            s += h_s_l[i]
            i += 1
            j += 1
        else:
            i += 1

        if s == needle:
            return i - len(needle)

    return -1
'''

def needle_in_haystack(haystack, needle):
    if needle == "":
        return 0

    for i in range(0, len(haystack) - len(needle) + 1):
        match = True
        for j in range(0, len(needle)):
            if haystack[i + j] != needle[j]:
                match = False
                break
        if match:
            return i

    return -1

print(needle_in_haystack("hello", "ll"))
print(needle_in_haystack("aaaaa", "abc"))
print(needle_in_haystack("haystack", ""))
print(needle_in_haystack("abc", "c"))
print(needle_in_haystack("mississippi", "issi"))

'''
Main Takeaways:
- Bug: Skipping potential match candidates
Let’s try this input:

python
Copy
Edit
haystack = "mississippi"
needle = "issi"
Your algorithm:

starts matching at index 1 ('i')

matches 'i' == 'i'

's' == 's'

's' == 's'

'i' == 'i'

Success! Returns 1 ✅

But now try:

python
Copy
Edit
haystack = "ababc"
needle = "abc"
Expected output: 2
Your algorithm will fail ❌. Why?

Because it does this:

i = 0: 'a' == 'a' → s = 'a', j = 1

i = 1: 'b' == 'b' → s = 'ab', j = 2

i = 2: 'a' != 'c' → doesn't reset j or s, just moves i forward

Now it starts from i=2, but doesn’t reset the search, so it can’t match the 'abc' starting at index 2.

- No reset on mismatch
If a mismatch occurs during matching, you must reset both s and j. Otherwise you carry forward partial matches 
incorrectly.

- Not optimal — extra space
You're building a s string as you go, which takes O(n) extra time and memory. You don’t need to build strings 
— just compare characters directly.

- The KMP is the full on optimal solution but is not needed in most interviews or compilers

- for i in range(len(haystack) - len(needle) + 1):
✅ What it does:
range(...) produces a sequence of numbers, starting at 0 by default.

It ends before it reaches the upper limit:
👉 len(haystack) - len(needle) + 1

📦 Why this specific limit?
We're sliding a window of size len(needle) over haystack.

For example:
If:

python
Copy
Edit
haystack = "abcdef"
needle = "cd"
We want to check substrings:

"ab" → starting at index 0

"bc" → index 1

"cd" → index 2 ✅

"de" → index 3

"ef" → index 4 ❌ (last valid start)

So:

len(haystack) = 6

len(needle) = 2

range(6 - 2 + 1) → range(5) → indexes 0 through 4
'''