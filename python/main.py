from calculator import my_functions as calc

def main():
    print("Choose Operation: ")
    print("0 -> Sum")
    print("1 -> Subtract")
    print("2 -> Divide")
    print("3 -> Multiply")

    op = int(input("Enter operation: "))
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    try:
        if op == 0:
            print("Result:", calc.sum_numbers(a, b))

        elif op == 1:
            if a == 0 or b == 0:
                raise ValueError("subtracting zero from Number")
            print("Result:", calc.subtract_numbers(a, b))

        elif op == 2:
            if b == 0:
                raise ZeroDivisionError("can't divide with zero")
            print("Result:", calc.divide_numbers(a, b))

        elif op == 3:
            if a == 0 or b == 0:
                raise ValueError("Multiply with Zero")
            print("Result:", calc.multiply_numbers(a, b))

        else:
            print("Invalid Operation!")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
