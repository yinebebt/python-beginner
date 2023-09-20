valid_operators = ["+", "-", "*", "/"]


def sum(arg1, arg2):
    return arg1 + arg2


def mul(arg1, arg2):
    return arg1 * arg2


def div(arg1, arg2):
    return arg1 / arg2


def sub(arg1, arg2):
    return arg1 - arg2


def main():
    try:
        num1 = float(input("enter first number:"))
        num2 = float(input('enter second number:'))
        opr = input('Enter operator:')
        if opr in valid_operators:
            if opr == "+":
                xsum = sum(num1, num2)
                print('result is:', xsum)
            elif opr == "-":
                xsub = sub(num1, num2)
                print('result is:', xsub)
            elif opr == "*":
                xmul = mul(num1, num2)
                print('result is:', xmul)
            elif opr == "/":
                xdiv = div(num1, num2)
                print('result is:', xdiv)
        else:
            print('operation is not valid')
    except:
        print('error occured')


main()
