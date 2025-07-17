'''🧩 Problem: Valid Palindrome II
Prompt:
Given a string s, return True if the string can be a palindrome after at most one character deletion, otherwise
return False.

🔧 Constraints:
1 <= len(s) <= 10⁵

String s contains only lowercase English letters.

Your solution should be O(n) time ideally.

You may not use extra space beyond a few pointers or constants.
'''
'''
Brute Force

def ValPal2(s):

    s_l = list(s)

    if s == "".join(s_l[::-1]):
        return True

    for i in range(0, len(s_l)):
        temp = s_l.pop(i)

        if s_l == s_l[::-1]:
            return True

        s_l.insert(i, temp)

    return False
'''

def ValPal2(s):
    def is_palindrome(i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            # Try skipping either the left or right character
            return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
        left += 1
        right -= 1

    return True

print(ValPal2("abca"))
print(ValPal2("racecar"))
print(ValPal2("abc"))

'''
Main Take Aways: 
- insert and pop are like c insertion and pops in dynamic arrays created with struct. They are O(n) each
because they shift n elements at the index location to either make room for or delete an element. O(n^2)
is too slow for the compilers in this case and they will crash out in larger strings

- Understand basic palindrome logic

- Using two pointer approach will help to make the algorithm faster
'''