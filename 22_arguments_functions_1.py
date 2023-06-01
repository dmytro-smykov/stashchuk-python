def merge_lists_to_dict(list_a, list_b):
    return dict(zip(list_a, list_b))


res_1 = merge_lists_to_dict(
    list_a=['ryzen 7', 'core i5', 'core i7'], list_b=[300, 250, 500])
print(res_1)

res_2 = merge_lists_to_dict(
    ['ryzen 7', 'core i5', 'core i7'], list_b=[300, 250, 500])
print(res_1)
