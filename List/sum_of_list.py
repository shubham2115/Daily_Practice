list_1 = [1, 2, 3, 4, 5]
list_2 = [6, 7, 8, 9, 10]


def sum_list(arr1, arr2):
    list_ = []
    for (a, b) in zip(arr1, arr2):
        list_.append(a + b)
    return list_


if __name__ == "__main__":
    list_out = sum_list(list_1, list_2)
    print(list_out)