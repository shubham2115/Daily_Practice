list_1 = [1, 3, 5, 7, 10]


def add_element(arr, element):
    for i in range(len(arr)):
        if arr[i] > element:
            arr.insert(i, element)
            return arr, i
    arr.append(element)
    return arr, len(arr)


list_out, index= add_element(list_1, 9)
print(list_out)
print(index)