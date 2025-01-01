from datetime import datetime
from collections import defaultdict
from file_manager import write_expense, read_expenses

def add_expense(category, amount, date):
    """Add an expense to the expenses file."""
    write_expense(category, amount, date)
    print("Expense added successfully!")

def view_expenses():
    """View all expenses categorized."""
    expenses = defaultdict(list)
    for category, amount, date in read_expenses():
        expenses[category].append((amount, date))
    
    print("Expenses:")
    for category, items in expenses.items():
        print(f"{category}:")
        if items:
            for i, (amount, date) in enumerate(items, start=1):
                print(f"  {i}. Amount: {amount} - Date: {date}")
        else:
            print("  No expenses recorded.")

def monthly_summary(year, month):
    """Generate a monthly summary of expenses."""
    total_expenses = 0
    category_summary = defaultdict(int)
    
    for category, amount, date in read_expenses():
        expense_date = datetime.strptime(date, '%Y-%m-%d')
        if expense_date.year == year and expense_date.month == month:
            total_expenses += float(amount)
            category_summary[category] += float(amount)
    
    print(f"Monthly Summary ({datetime(year, month, 1).strftime('%B %Y')}):")
    print(f"Total Expenses: {total_expenses}")
    print("By Category:")
    for category, total in category_summary.items():
        print(f"{category}: {total}")

def delete_expense(category, amount, date):
    """Delete a specific expense from the expenses file."""
    expenses = read_expenses()
    with open('expenses.txt', 'w') as f:
        for exp in expenses:
            if exp != [category, amount, date]:
                f.write(','.join(exp) + '\n')
    
    print("Expense deleted successfully!")