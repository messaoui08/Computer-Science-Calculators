import hashlib
import os
from rich.console import Console
from rich.text import Text
from rich.panel import Panel

# Initialize the Rich Console
console = Console()

USER_FILE = "data/users.txt"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login_or_register():
    console.print("\n--- [bold magenta]Login or Register[/bold magenta] ---")
    choice = input("[1]. Login\n[2]. Create Account\nChoose (1/2): ")
    if choice == "1":
        return login()
    elif choice == "2":
        return create_account()
    else:
        console.print("[bold red]Invalid choice.[/bold red]")
        return None

def login():
    console.print("[bold cyan]Login[/bold cyan] - Please enter your details.")
    username = input("Enter username: ")
    password = input("Enter password: ")
    hashed = hash_password(password)
    users = read_users()

    if username in users and users[username] == hashed:
        console.print(f"[bold green]Welcome back, {username}![/bold green]")
        return username
    console.print("[bold red]Invalid username or password.[/bold red]")
    return None

def create_account():
    console.print("[bold cyan]Create Account[/bold cyan] - Please choose your details.")
    username = input("Choose a username: ")
    password = input("Choose a password: ")
    hashed = hash_password(password)
    users = read_users()

    if username in users:
        console.print("[bold red]Username already exists.[/bold red]")
        return None
    users[username] = hashed
    write_users(users)
    console.print(f"[bold green]Account created for {username}![/bold green]")
    return username

def read_users():
    """Read user data from the text file."""
    if not os.path.exists(USER_FILE):
        return {}
    with open(USER_FILE, "r") as file:
        return dict(line.strip().split(":", 1) for line in file if ":" in line)

def write_users(users):
    """Write user data to the text file."""
    with open(USER_FILE, "w") as file:
        for username, hashed_password in users.items():
            file.write(f"{username}:{hashed_password}\n")

