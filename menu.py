from core.conversion import transform_number
from core.ip_calc import compute_ip_planning

def display_menu():
    while True:
        print("\nMain Menu:")
        print("1. Transform Number Systems")
        print("2. Compute IP Planning")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            transform_number()
        elif choice == "2":
            compute_ip_planning()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")
