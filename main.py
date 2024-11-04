import string

def check_numbers(info):
    for i in info:
        if i in numbers:
            return True
    return False

password = input("Please enter your password")
print(f"Your password is {password}")

#adding variables
numbers = "0123456789"
letters = string.ascii_letters
special_symbols = "!@#$%^&*<>?/|{}"
