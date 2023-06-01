def dict_to_list(dict):
    list_for_conversion = []
    for key, value in dict.items():
        if type(value) == int:
            value *= 2
        list_for_conversion.append((key, value))
    return list_for_conversion


print(dict_to_list({'a': 1, 'b': 2}))
