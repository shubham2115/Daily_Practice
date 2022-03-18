list_ = [1, 2, 5, -4, -6, 7, -9, 2]


def pos_neg(arr):
    sum_pos = 0
    sum_neg = 0
    for i in arr:
        if i >= 0:
            sum_pos += i
        if i < 0:
            sum_neg += i
    return sum_neg, sum_pos


if __name__ == "__main__":
    sum1, sum2 = pos_neg(list_)
    print(f"Sum of Positive number in a given List:{sum2}")
    print(f"Sum of Negative number in a given List:{sum1}")