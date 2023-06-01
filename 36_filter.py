def filter_list(list, item_type):
    result_list = []
    for item in list:
        if item_type == type(item):
            result_list.append(item)
    return result_list


def filter_list_2(list_to_filter, value_type):
    def check_element_type(element):
        return type(element) is value_type
    return list(filter(check_element_type, list_to_filter))


print(filter_list([1, 'ab', 3, True], int))
print(filter_list_2([1, 'ab', 3, True], int))
