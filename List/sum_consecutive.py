list_ = [1, 2, 4, 8, 6, 3, 7, 8, 6]
out_list = []

for i in range(0, len(list_), 2):
    if (i+1) < len(list_):
        sum = list_[i] + list_[i+1]
    else:
        sum = list_[i]
    out_list.append(sum)

print(out_list)