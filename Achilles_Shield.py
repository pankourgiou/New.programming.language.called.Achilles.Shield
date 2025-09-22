import os
import random
import sys

# --- Command Functions ---
def greet(*args):
    """Greet the user"""
    name = args[0] if args else "Hero"
    print(f"Hello, {name}! Welcome to Achilles Shield.")

def add(*args):
    """Add numbers"""
    try:
        numbers = [float(x) for x in args]
        print("Sum:", sum(numbers))
    except ValueError:
        print("Error: all arguments must be numbers.")

def multiply(*args):
    """Multiply numbers"""
    try:
        result = 1
        for n in args:
            result *= float(n)
        print("Product:", result)
    except ValueError:
        print("Error: all arguments must be numbers.")

def analyze(*args):
    """Simple text analysis"""
    text = " ".join(args)
    word_count = len(text.split())
    char_count = len(text)
    print(f"Text Analysis -> Words: {word_count}, Characters: {char_count}")

def read(*args):
    """Read a file"""
    if not args:
        print("Error: specify a file name")
        return
    filename = args[0]
    if not os.path.isfile(filename):
        print(f"File not found: {filename}")
        return
    with open(filename, "r") as f:
        content = f.read()
    print(f"--- Contents of {filename} ---\n{content}")

def write(*args):
    """Write text to a file"""
    if len(args) < 2:
        print("Error: specify a file name and text")
        return
    filename = args[0]
    text = " ".join(args[1:])
    with open(filename, "w") as f:
        f.write(text)
    print(f"Written to {filename}")

def random(*args):
    """Generate a random number"""
    if len(args) == 2:
        try:
            low = int(args[0])
            high = int(args[1])
            print("Random Number:", random.randint(low, high))
        except ValueError:
            print("Error: provide two integer numbers")
    else:
        print("Random Number:", random.random())

def echo(*args):
    """Echo the input"""
    print(" ".join(args))

def help(*args):
    """Show help for commands"""
    print("Achilles Shield Commands:")
    for cmd, func in COMMANDS.items():
        print(f" - {cmd}: {func.__doc__}")
    print(" - help: Show this help message")
    print(" - exit: Exit the REPL")

def exit(*args):
    """Exit the REPL"""
    print("Exiting Achilles Shield REPL.")
    sys.exit(0)

def unknown_command(cmd, *args):
    print(f"Unknown command: {cmd}")

# --- Command Registry ---
COMMANDS = {
    "greet": greet,
    "add": add,
    "multiply": multiply,
    "analyze": analyze,
    "read": read,
    "write": write,
    "random": random,
    "echo": echo,
    "help": help,
    "exit": exit
}

# --- Interpreter ---
def execute_line(line):
    line = line.strip()
    if not line or line.startswith("#"):
        return
    parts = line.split()
    cmd = parts[0].lower()
    args = parts[1:]
    if cmd in COMMANDS:
        COMMANDS[cmd](*args)
    else:
        unknown_command(cmd, *args)

def run_achilles_shield(file_path):
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        return
    with open(file_path, "r") as f:
        for line in f:
            execute_line(line)

# --- REPL ---
def start_repl():
    print("Achilles Shield REPL - Type 'help' for commands, 'exit' to quit.")
    while True:
        try:
            line = input(">> ")
            execute_line(line)
        except (KeyboardInterrupt, EOFError):
            print("\nExiting REPL.")
            break

# --- Main ---
if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_achilles_shield(sys.argv[1])
    else:
        start_repl()
