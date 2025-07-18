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

def needle_in_haystack(haystack ,needle):
    h_s_l = list(haystack)
    n_s_l = list(needle)

    if needle == "":
        return 0

    for i in range(0, len(h_s_l)):
        s = ""
        for j in range(i, len(n_s_l)):
            print(j)
            if n_s_l[j] == h_s_l[j]:
                s += n_s_l[j]

        if s == needle:
            print(i, s)
            return i

    return -1

print(needle_in_haystack("hello", "ll"))
#print(needle_in_haystack("aaaaa", "abc"))
#print(needle_in_haystack("haystack", ""))
#print(needle_in_haystack("mississippi", "issi"))
