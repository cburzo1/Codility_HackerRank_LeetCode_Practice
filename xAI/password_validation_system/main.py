import re

def password_validation(pw):
    if len(pw) < 8:
        return False

    #pw2 = re.sub(r'[0-9]', '', pw)
    pw2 = re.findall(r'[0-9]+', pw)
    print(pw2)
    if len(pw2) < 1:
        return False

    return True

    #print(pw2)

print(password_validation("Abcdef1!"))
print(password_validation("abc1!"))
print(password_validation("ABCDEF123"))
print(password_validation("Abc def1!"))
print(password_validation("ValidPass1@"))
print(password_validation("ValidPass@"))
