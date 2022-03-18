string_ = "Hello, How are you?"
dict_ = {}

for i in string_:
    if i not in dict_.keys():
        dict_[i] = 1
    else:
        dict_[i] += 1

print(dict_)