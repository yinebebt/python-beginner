#Q.2
str = "kiburcollege"
for i in range(len(str)):
    if i%2 ==0:
        print(str[i])

# Q.3
numbers = [10, 20, 33, 46, 55]
print("Divisible by 5")
for num in numbers:
    if num % 5 == 0:
        print(num)

# Q.5
integer_input = int(input("Enter an integer: "))
reversed_digits = ""
# Extract and reverse the digits
while integer_input > 0:
    digit = integer_input % 10  # Get the last digit
    reversed_digits += str(digit) + " "
    integer_input //= 10  # Remove the last digit, floor division
print("Reversed digits:", reversed_digits.strip())


# Q.6
income = int(input("Enter taxable income: $"))

tax_rate_1 = 0.0  # Rate for the first $10,000
tax_rate_2 = 0.10  # next $10,000
tax_rate_3 = 0.20  # remaining income

tax_payable = 0.0  # Initialize tax_payable to 0

# Calculate tax payable based on the rules
if income <= 10000:
    tax_payable = income * tax_rate_1
elif income <= 20000:
    tax_payable = (10000 * tax_rate_1) + ((income - 10000) * tax_rate_2)
else:
    tax_payable = (10000 * tax_rate_1) + (10000 * tax_rate_2) + \
        ((income - 20000) * tax_rate_3)

print(f"Income tax payable: ${tax_payable:.2f}")
