list_ = [1, 5, 8, 12, 3, 17, 13]


def get_min_max(arr, k, min=True):
    arr.sort()
    if min:
        return arr[k - 1]
    if not min:
        return arr[-k]


if __name__ == "__main__":
    out = get_min_max(list_, 2)
    print(out)
    out_ = get_min_max(list_, 2, min=False)
    print(out_)
