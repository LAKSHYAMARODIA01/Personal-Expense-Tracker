import os

EXPENSES_FILE = 'expenses.txt'

def initialize_expenses_file():
    """Create the expenses file if it doesn't exist."""
    if not os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, 'w') as f:
            f.write('')  # Create an empty file

def read_expenses():
    """Read expenses from the file and return a list of expenses."""
    expenses = []
    with open(EXPENSES_FILE, 'r') as f:
        for line in f:
            expenses.append(line.strip().split(','))
    return expenses

def write_expense(category, amount, date):
    """Write a new expense to the expenses file."""
    with open(EXPENSES_FILE, 'a') as f:
        f.write(f"{category},{amount},{date}\n")


