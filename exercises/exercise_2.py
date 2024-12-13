'''
# Q.2
def remove_chars(string, n):
    if n < 0:
        return string
    return string[n:]


upd_str= remove_chars("kiburcollege", 5)
# Q.3


def halfPyr(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print('*', end='')
        print()


halfPyr(5)

# Q.4


def exp(a, b):
    if b < 0:
        print("b need to be non-negative number")
        return -1
    exp = 1
    for i in range(b):
        exp *= a
    return exp


print(exp(5, 4))

# Q.5
num = int(input("Enter a number: "))
sum = 0
for i in range(num):
    sum += i+1
print(f'The sum from 1 to {num} is {sum}')


# Q.6
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num % 5 == 0:
        if (num > 150):
            continue
        elif (num > 500):
            break
        else:
            print(num)
'''

# Q. 7
num1 = 0
num2 = 1
print(num1, num2, end=" ")
for i in range(8):
    num3 = num1 + num2
    print(num3, end=" ")
    num1, num2 = num2, num3
