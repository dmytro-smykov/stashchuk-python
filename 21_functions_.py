def merge_lists_to_dict(list_a, list_b):
    result = zip(list_a, list_b)
    return dict(result)


print(merge_lists_to_dict(['ryzen 7', 'core i5', 'core i7'], [300, 250, 500]))
