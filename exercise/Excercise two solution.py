#Excercise2 
#question number one 
'''prev_num=0
for i in range(1,11):
    xsum=prev_num + i
    print('Current number is:',i,'Previous Number is:',prev_num, 'the sum is:',xsum)
    prev_num=i

#Question Number two
word=input("Enter your string:")
length=len(word)
for i in range(0,length-1,2):
    print ('current character is:',word[i])

#using list slicing 
ls1=list(word)
print(ls1[0::2])


#Question Number 4

for i in range(10):
    for num in range(i):
        print(i,end=' ')
    print('\n')

#Question number 3

num_list = [10, 20, 33, 46, 55]
print("Given list:", num_list)
print('Divisible by 5:')
for num in num_list:
    if num % 5 == 0:
        print(num)

#Excercise 5
num=7536
while num>0:
    digit=num %10
    num = num // 10
    print(digit,end=" ")

#Excercise 6
income = 45000
tax_payable = 0
print("Given income", income)

if income <= 10000:
    tax_payable = 0
elif income <= 20000:
    # no tax on first 10,000
    x = income - 10000
    # 10% tax
    tax_payable = x * 10 / 100
else:
    # first 10,000
    tax_payable = 0

    # next 10,000 10% tax
    tax_payable = 10000 * 10 / 100

    # remaining 20%tax
    tax_payable += (income - 20000) * 20 / 100

print("Total tax to pay is", tax_payable)
tup=[3,'love','you','more']
l=len(tup)
for i in range(0,l,2):
    print(tup[i])'''

