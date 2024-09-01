
import calculation as cal
import options as opt


def main():
    opt.calculator()
    cal.endl()


    print("If You Want More Calculation Press 1 👇👇👇")
    print("1. YES")
    print("2. NO")

        #global cheak
    cheak = input("Press YES for 1 && NO for 2: ")


    if cheak in "1":
             main()
    elif cheak =="2":

             print (".......Your Calculation is:")
    else:
            print("....😢😢....Invalid Input....😢😢...")


if __name__ == '__main__':
    main()