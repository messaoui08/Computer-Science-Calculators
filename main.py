from core.auth import authenticate_user
from core.menu import display_menu

def main():
    print("Welcome to the Computer Science Calculator!")
    if authenticate_user():
        display_menu()

if __name__ == "__main__":
    main()
