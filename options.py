import calculation as cal

def calculator():
    print("Selec Operation: ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
   # print("5. Exit")

    option=input("Enter your choice (1/2/3/4): ")
    if option in ("1","2","3","4"):
        num1=float(input("Enter 1st Number: "))
        num2=float(input("Enter 2nd Number: "))

        if option=="1":
            print(cal.add(num1,num2))

        elif option=="2":
            print(cal.sub(num1,num2))

        elif option=="3":
            print(cal.mul(num1,num2))

        elif option=="4":
            print(cal.div(num1,num2))

        #elif option=="5":
        else:
            print("Invalid Input")



