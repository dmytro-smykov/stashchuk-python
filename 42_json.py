import json


dict1 = {'color': 'black',
         'age': 5,
         'Good': True}

json_dict = json.dumps(dict1)

print(json_dict)
print(type(json_dict))
