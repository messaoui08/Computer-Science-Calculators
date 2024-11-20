def transform_number():
    print("1. Binary to Decimal")
    print("2. Decimal to Binary")
    print("3. Octal to Decimal")
    print("4. Hexadecimal to Decimal")
    choice = input("Choose an option: ")
    number = input("Enter the number: ")
    try:
        if choice == "1":
            print(f"Decimal: {int(number, 2)}")
        elif choice == "2":
            print(f"Binary: {bin(int(number))[2:]}")
        elif choice == "3":
            print(f"Decimal: {int(number, 8)}")
        elif choice == "4":
            print(f"Decimal: {int(number, 16)}")
        else:
            print("Invalid choice!")
    except ValueError:
        print("Invalid number format!")
