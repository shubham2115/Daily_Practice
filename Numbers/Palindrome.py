number = 16161

rev = str(number)[::-1]

if number == int(rev):
    print("Number is a Palindrome")
else:
    print("Number is not Palindrome")