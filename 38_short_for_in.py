car = {'brand': 'bmw', 'transmission': 'auto'}
car_2 = {k: v.upper() for k, v in car.items()}
print(car_2)

list = ['bmw', 'ferrari', 'abc', 'mercedes']
list_2 = [i for i in list if len(i) > 3]
print(list_2)
