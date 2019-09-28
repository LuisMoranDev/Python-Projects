
def binaryCalc():

    while True:

        try:
            calcType = input(
                "Would you like to convert a number to binary or decimal number? ")
            calcType = calcType.lower()
        except:
            print("Please enter answer")

        else:
            if "bi" in calcType or "dec" in calcType:
                break

            else:
                print("Must enter binary or decimal")

    if "bi" in calcType:
        n = int(input("Enter the hexadecimal number to convert binary: "))
        n = str(bin(n))
        n = n.replace("0b", "")
        print("The binary number is: " + n)

    else:
        n = int(input("Enter the binary number to convert to hexadecimal: "), 2)

        print(f"The hexadecimal is: {n}")


binaryCalc()
