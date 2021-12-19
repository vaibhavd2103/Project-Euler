"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million.
Find the sum of the even-valued terms.
"""

a = 1
b = 0
sum_of_2 = 0
sum = 0

range_ = int(
    input("Enter the number up to which you want to calculate -------> "))

for i in range(range_):
    if sum_of_2 < range_:
        i = a + b
        b = a
        a = i
        sum_of_2 = i
        if sum_of_2 % 2 == 0:
            sum = sum + sum_of_2

print(
    f'The sum of the even-valued terms of Fibonacci series calculated up to {range_} is {sum}')
