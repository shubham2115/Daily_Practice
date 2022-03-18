list_1 = [1, 3, 5, 7, 10]
list_2 = [2, 4, 9]


def add_element(arr_1, arr_2):
    index_ = []
    for j in range(len(arr_2)):
        flag = False
        for i in range(len(arr_1)):
            if arr_2[j] < arr_1[i]:
                arr_1.insert(i, arr_2[j])
                index_.append(i)
                flag = True
                break
        if not flag:
            arr_1.append(arr_2[j])
    return arr_1, index_


if __name__ == "__main__":
    out_list, index_out = add_element(list_1, list_2)
    print(out_list)
    print(index_out)