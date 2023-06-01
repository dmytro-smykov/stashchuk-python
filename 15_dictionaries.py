new_dict = {}

for i in range(3):
    key = input(f'Введите название ключа: ')
    value = int(input(
        f'Введите значение ключа: '))
    new_dict[key] = value


print(new_dict)
