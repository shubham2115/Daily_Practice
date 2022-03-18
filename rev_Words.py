string_ = "Hello, How are you?"
rev_string = ''

for word in string_.split(' '):
    rev_string += word[::-1] +' '

print(rev_string)