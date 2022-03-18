num = 71

temp = num
sum = 0

while temp > 0:
    number = temp % 10
    sum += number ** len(str(num))
    temp = temp//10

print(sum == num)