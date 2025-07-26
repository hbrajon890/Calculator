print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")
option = float(input("Choose an operation: "))

if(option in [1,2,3,4]):
    number1 = float(input("Enter the first number:"))
    number2 = float(input("Enter the second number: "))

    if(option == 1):
        result = number1 + number2
    elif(option == 2):
        result = number1 - number2 
    elif(option == 3):
        result= number1 * number2
    elif(option == 4):
        result = number1 / number2    #// mane sudu int 



else:
    print("Invalid number")

print(f"the result of this operation is : {result}")