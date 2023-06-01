# while True:
#    num_1 = float(input("Введите первое число: "))
#    num_2 = float(input("Введите второе число: "))
#    print(num_1/num_2)
#    repeat = input("Продолжить? yes/no: ")
#    if repeat == 'yes':
#        continue
#    break


while True:
    num_1 = float(input("Введите первое число: "))
    num_2 = float(input("Введите второе число: "))

    print(num_1/num_2)

    repeat = input("Продолжить? yes/no: ")
    if repeat == 'no':
        break
