#Q1
'''def multiplication_or_sum(num1, num2):
    # calculate product of two number
    product = num1 * num2
    # check if product is less then 1000
    if product <= 1000:
        return product
    else:
        # product is greater than 1000 calculate sum
        return num1 + num2

# first condition
result = multiplication_or_sum(20, 30)
print("The result is", result)

# Second condition
result = multiplication_or_sum(40, 30)
print("The result is", result)



#Q2
def remove_chars(word, n):
    print('Original string:', word)
    x = word[n:]
    return x

print("Removing characters from a string")
print(remove_chars("Kiburcollege", 4))
print(remove_chars("Kiburcollege", 2))



#Q3
for i in range(6, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")


#Q4
def exponent(base, exp):
    num = exp
    result = 1
    while num > 0:
        result = result * base
        num = num - 1
    print(base, "raises to the power of", exp, "is: ", result)

exponent(5, 4)


#Ex5
# s: store sum of all numbers
s = 0
n = int(input("Enter number "))
# run loop n times
# stop: n+1 (because range never include stop number in result)
for i in range(1, n + 1, 1):
    # add current number to sum variable
    s += i
print("\n")
print("Sum is: ", s)


#Ex6
numbers = [12, 75, 150, 180, 145, 525, 50]
# iterate each item of a list
for item in numbers:
    if item > 500:
        break
    elif item > 150:
        continue
    # check if number is divisible by 5
    elif item % 5 == 0:
        print(item)


#Ex7
num1, num2 = 0, 1

print("Fibonacci sequence:")
# run loop 10 times
for i in range(10):
    # print next number of a series
    print(num1, end="  ")
    # add last two numbers to get next number
    res = num1 + num2

    # update values
    num1 = num2
    num2 = res
'''

valid_operators = ["+", "-", "*", "/"]


def sum(arg1,arg2):
    return arg1 + arg2

def mul(arg1,arg2):
    return arg1 * arg2

def div(arg1,arg2):
    return arg1 / arg2

def sub(arg1,arg2):
    return arg1 - arg2


def main():
    try:
        in1 = float(input("enter first number:"))
        in2 = float(input('enter second number:'))
        op = input('Enter operator:')
        if op in valid_operators:
            if op=="+":
                xsum = sum(in1, in2)
                print('result is:', xsum)
            elif op=="-":
                xsub = sub(in1, in2)
                print('result is:', xsub)
            elif op=="*":
                xmul = mul(in1, in2)
                print('result is:', xmul)
            elif op=="/":
                xdiv = div(in1, in2)
                print('result is:', xdiv)
        else:
            print('operation is not valid')
    except:
        print('error occured')

main()






