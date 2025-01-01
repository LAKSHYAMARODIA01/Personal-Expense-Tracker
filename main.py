from file_manager import initialize_expenses_file
from expense_manager import add_expense, view_expenses, monthly_summary, delete_expense

def main():
    initialize_expenses_file()
    
    while True:
        print("\nWelcome to Personal Expense Tracker!")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Delete Expense")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            category = input("Enter category (e.g., Food, Travel): ")
            amount = input("Enter amount: ")
            date = input("Enter date (YYYY-MM-DD): ")
            add_expense(category, amount, date)
        
        elif choice == '2':
            view_expenses()
        
        elif choice == '3':
            year = int(input("Enter year (YYYY): "))
            month = int(input("Enter month (1-12): "))
            monthly_summary(year, month)
        
        elif choice == '4':
            category = input("Enter category of the expense to delete: ")
            amount = input("Enter amount of the expense to delete: ")
            date = input("Enter date (YYYY-MM-DD) of the expense to delete: ")
            delete_expense(category, amount, date)
        
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()