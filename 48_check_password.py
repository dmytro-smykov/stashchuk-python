import re


def password_check(password):
    lenght = re.compile(r"\S{8,}")
    uppercase = re.compile(r"^.*[A-Z]+.*$")
    lowercase = re.compile(r"^.*[a-z]+.*$")
    numbers = re.compile(r"^.*[0-9]+.*$")
    cymbols = re.compile(r"^.*[*@#$%^&+=!^]+.*$")
    spaces = re.compile(r"^\S*$")
    message = []
    if not spaces.fullmatch(password):
        message.append('В пробеле не должно быть пробелов')
    if not lenght.fullmatch(password):
        message.append('В пароле должно быть не менее 8-и символов')
    if not uppercase.fullmatch(password):
        message.append(
            'В пароле должна быть хотябы одна буква верхнего регистра')
    if not lowercase.fullmatch(password):
        message.append(
            'В пароле должна быть хотябы одна буква нижнего регистра')
    if not numbers.fullmatch(password):
        message.append('В пароле должна быть хотябы одна цифра')
    if not cymbols.fullmatch(password):
        message.append('В пароле должен быть хотябы один символ')
    return (message)


# print(password_check(input('enter password: ')))
print(password_check('ooOO123!jdhjJh'))
print(password_check('o1!jj'))
