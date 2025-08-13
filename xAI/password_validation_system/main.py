import re

def password_validation(pw):
    if len(pw) < 8:
        return False

    if not re.search(r'[a-z]', pw):
        return False
    if not re.search(r'[A-Z]', pw):
        return False
    if not re.search(r'[0-9]', pw):
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
