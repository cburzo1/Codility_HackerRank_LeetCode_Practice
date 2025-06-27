def valid_par(st):
    if len(st) <= 1:
        return False

    s = list(st)

    if s[0] == ")" or s[0] == "}" or s[0] == "]":
        return False

    stk = [s[0]]

    i = 1

    #print(stk[len(stk) - 1])

    while i < len(s):
        if s[i] == "(" or s[i] == "{" or s[i] == "[":
            stk.append(s[i])
        else:
            if len(stk) == 0:
                return False
            '''
                This is important to understand because for inputs like this, "(()))", the stack will
                be empty yet it will still check the stack without this line. This causes index out of
                bounds error that cannot be avoided.
            '''

            if s[i] == ")" and stk[len(stk) - 1] == "(":
                stk.pop()
            elif s[i] == "}" and stk[len(stk) - 1] == "{":
                stk.pop()
            elif s[i] == "]" and stk[len(stk) - 1] == "[":
                stk.pop()
            else:
                return False  # Mismatched closing bracket

        i += 1

    return len(stk) == 0

print(valid_par("()"))
print(valid_par("()[]{}"))
print(valid_par("(]"))
print(valid_par("([)]"))
print(valid_par("{[]}"))
print(valid_par("{[{}"))

'''
Main Take Aways:
- Stack Pattern for Matching Pairs
Use a stack to track opening characters (or events) until a corresponding closing one arrives.

Works well for:

Matching brackets ()[]{}

XML/HTML tag validation

Parsing expressions

DFS traversal with backtracking

💡 Think of a stack as your “trail of breadcrumbs” — when something closes, it must match what most recently opened.

2. Early Termination on Invalid State
Always check if the stack is empty before popping or peeking (stk[-1]) — protects against errors like:

Unbalanced input (")(")

Premature closing without a match ("]" before a "[")

🔒 Defensive coding: never assume something is in the stack unless you check it.

3. Immediate Return on Mismatch
If a closing bracket doesn't match the top of the stack → it's an invalid sequence.

Return False immediately for mismatches. Don’t wait till the end.

⚠️ Failing early saves time and avoids unnecessary computation.

4. Final Stack Check After Loop
After processing all characters:

If the stack is not empty, then you have unmatched opening brackets → return False.

If the stack is empty, all matches were balanced → return True.

🧹 Think of the stack as your leftover clutter: if it’s not cleaned up at the end, something went wrong.

5. Avoid Redundant Checks Outside Loop
You don’t necessarily need to check s[0] before the loop. The main logic can handle it inside the loop with proper stack length checks.

This simplifies your code and avoids hardcoding special cases.
'''