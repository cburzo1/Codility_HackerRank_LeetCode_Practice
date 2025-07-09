'''def string_compression(s):

    s1 = list(s)
    count = 0
    s2 = ""

    for i in range(0, len(s)):
        count += 1

        if s[i] != s[i - 1] and s[i - 1] is not None:
            s2 += s[i - 1] + str(count)
            count = 0

    print(s2)

    return s2'''

def string_compression(s):
    if len(s) == 0:
        return ""

    s2 = ""
    count = 1  # Start at 1 since we already "have" the first character

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            s2 += s[i - 1] + str(count)
            count = 1  # Reset count for new char

    # Add the final group after loop
    s2 += s[-1] + str(count)

    return s2

print(string_compression("aabcccccaaa"))
#a2b1c5a3

'''
Main Take Aways: 
- Tracking Runs / Groups in a Sequence
Core idea: identify and process consecutive identical elements.

This is a recurring pattern in many problems (e.g., run-length encoding, word grouping, string parsing, image compression, etc.).

🔁 Takeaway: Learn to track when a value starts/ends a group, and handle each group fully before moving on.

- Proper Loop Control with Conditions
You need to make decisions at the right time inside a loop.

Specifically:

Keep a counter while values are the same.

Reset and store result when the value changes.

🔁 Takeaway: Understand where and when to flush accumulated logic (e.g., in if blocks or after the loop ends).

- Handling the Final Group After the Loop
Many beginners forget to append the last group (since it doesn’t hit the change condition).

🔁 Takeaway: After any loop that’s watching for a change, always ask: "Do I need to handle leftovers after the loop?"

- Efficient String Building in Python
Using += to build strings repeatedly creates new strings, which is inefficient in large-scale problems.

🔁 Takeaway: Prefer list.append() followed by "".join() for better performance in large datasets.
'''