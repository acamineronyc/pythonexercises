# Store the user input of two numbers and the operator
num1, operator, num2 = input("Enter Calculation: ").split()

# Convert the strings into integers
num1 = int(num1)
num2 = int(num2)

# Print the result
if operator == "+":
    print("{0} + {1} = {2}".format(num1, num2,  num1 + num2))
elif operator == "-":
    print("{0} - {1} = {2}".format(num1, num2, num1 - num2))
elif operator == "*":
    print("{0} * {1} = {2}".format(num1, num2, num1 * num2))
elif operator == "/":
    print("{0} - {1} = {2}".format(num1, num2, num1 - num2))
elif operator == "%":
    print("{0} % {1} = {2}".format(num1, num2, num1 % num2))
else:
    print("Enter a valid operation: +, -, *, /, or %")