import math
print("="*35)
print("         SIMPLE CALCULATOR             ")
print("="*35)
while True:
    print("\nChoose an operation")
    print(" 1. Addition")
    print(" 2. Subtraction")
    print(" 3. Multiplication")
    print(" 4. Division")
    print(" 5. Exit")

    choice=input("\nEnter your Choice(1-5):")

    if choice=="1":
        num1=float(input("Enter the first number:"))
        num2=float(input("Enter the second number:"))
        print("Result=",num1+num2)
    elif choice=="2":
        num1=float(input("Enter the first number:"))
        num2=float(input("Enter the second number:"))
        print("Result=",num1-num2)
    elif choice=="3":
        num1=float(input("Enter the first number:"))
        num2=float(input("Enter the second number:"))
        print("Result=",num1*num2)
    elif choice=="4":
        num1=float(input("Enter the first number:"))
        num2=float(input("Enter the second number:"))

        if num2 !=0:
            print("Result=",num1/num2)
        else:
            print("Error! Division by zero is not allowed.")   
        break 
    elif choice=="5":
        print("\nThank you for using the Calculator! ")
        break   
    else:
        print("Invalid Choice! Please select a valid option.")
        break         

print("-"*35)                   