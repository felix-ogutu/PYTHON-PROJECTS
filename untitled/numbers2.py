# programme to swap two numbers
x = 5
y = 6
# create a temporary variable and swap the values
temp = x
x = y
y = temp
print('The value of x after swapping :{}'.format(x))
print('The value of y after swapping : {}'.format(y))

# programme to swap numbers without temporary variable
number1 = int(input("Enter the first number:"))
number2 = int(input("Enter the second number:"))
# to swap the numbers using addition and subtraction
number1 = number1 + number2
number2 = number1 - number2
number1 = number1 - number2
print("The value of the number1 after swapping : {} ".format(number1))
print("The value of the number2 after swapping :  {} ".format(number2))

