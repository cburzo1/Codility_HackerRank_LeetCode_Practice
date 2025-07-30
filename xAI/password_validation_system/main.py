'''import re

def password_validation(pw):
    pwlc = re.findall(r'[a-z]+', pw)
    if len(pwlc) < 1:
        return False

    pwuc = re.findall(r'[A-Z]+', pw)
    if len(pwuc) < 1:
        return False

    if len(pw) < 8:
        return False

    pwi = re.findall(r'[0-9]+', pw)

    if len(pwi) < 1:
        return False

    #pwsc = re.findall(r'[^a-zA-Z0-9_]', pw)
    pwsc = re.findall(r'[\W]', pw)

    if len(pwsc) < 1:
        return False

    pwws = re.findall(r'[\s]', pw)

    if len(pwws) > 0:
        return False

    return True'''

import re

def password_validation(pw):
    if len(pw) < 8:
        return False

    if not re.search(r'[a-z]', pw):
        return False
    if not re.search(r'[A-Z]', pw):
        return False
    if not re.search(r'\d', pw):
        return False
    if not re.search(r'[!@#$%^&*()\-+]', pw):
        return False
    if re.search(r'\s', pw):  # check for spaces
        return False

    return True

print(password_validation("Abcdef1!"))
print(password_validation("abc1!"))
print(password_validation("ABCDEF123"))
print(password_validation("Abc def1!"))
print(password_validation("ValidPass1@"))
print(password_validation("ValidPass@"))
print(password_validation("isValid@!1"))
