try:
    n1 = input()
    n2 = input()

    n3 = int(n1) + int(n2)

    print(n3)
    print(int(n1)/int(n2))
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")

