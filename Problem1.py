# To print all the multiples of 3 and 5 below 1000

a = 3
b = 5
sum = 0
till = int(input("Enter the number up to which you want to find the sum ------> "))

for i in range(till):
    if i % 3 == 0 and i % 5 == 0:
        sum = sum + i
    elif i % 5 == 0:
        sum = sum + i
    elif i % 3 == 0:
        sum = sum + i
print(
    f'The sum of all numbers below {till} divisible by 3, 5 and both is ------> {sum}')
