import re


def password_check(password):
    lenght = re.compile(r"\S{8,}")
    uppercase = re.compile(r"^.*[A-Z]+.*$")
    lowercase = re.compile(r"^.*[a-z]+.*$")
    numbers = re.compile(r"^.*[0-9]+.*$")
    cymbols = re.compile(r"^.*[*@#$%^&+=^]+.*$")
    if not lenght.fullmatch(password):
        return (False, 'Password is too short')
    if not uppercase.fullmatch(password):
        return (False, 'Password must have uppercase letter')
    if not lowercase.fullmatch(password):
        return (False, 'Password must have lowercase letter')
    if not numbers.fullmatch(password):
        return (False, 'Password must have numbers')
    if not cymbols.fullmatch(password):
        return (False, 'Password must have cymbols')
    return (True, "Password is valid")


print(password_check(input('enter password: ')))
