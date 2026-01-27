import re

passwords = ["abc", "123456", "Pass@123", "Admin","User@2021", "weakpwd", "Strong#1"]

def validate_password(pwd):
    if len(pwd) < 8:
        return False
    if not re.search(r"[0-9]", pwd):
        return False
    if not re.search(r"[@#$%^&*!]", pwd):
        return False
    return True

print("Password Strength Report\n")

for pwd in passwords:
    if validate_password(pwd):
        print(pwd, "=> PASS")
    else:
        print(pwd, "=> FAIL")
