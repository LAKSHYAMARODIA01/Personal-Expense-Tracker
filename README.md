# Personal Expense Tracker

📊 A simple and intuitive Personal Expense Tracker that helps you manage your finances by recording, categorizing, and summarizing your expenses. This application is designed to provide insights into your spending habits, making it easier to stay on top of your budget.

## Features Implemented

- **Add Expense**: Easily add expenses with a category, amount, and date using command-line arguments.
- **View Expenses**: View all recorded expenses categorized neatly in the console.
- **Monthly Summary**: Generate a summary of expenses for a specific month and year, showing total expenses and a breakdown by category.
- **Persistent Storage**: Expense data is stored in a text file (`expenses.txt`), ensuring data retention between sessions.
- **Command-Line Interface**: Use simple commands to interact with the application, making it user-friendly.
- **Delete Expense**: Remove an expense by specifying its index.
- **Category Filtering**: View expenses filtered by a specific category.

## How to Run the Project

1. **Clone the Repository**: Clone the repository to your local machine using:
   ```bash
   git clone https://github.com/LAKSHYAMARODIA01/Personal-Expense-Tracker.git
2. **Navigate to the Project Directory**:
     ```bash
     cd Personal-Expense-Tracker
3. **Install Dependencies**: This project requires the colorama library for enhanced console visuals. Install it using pip:
      ```bash
      pip install colorama
4. **Run the Application**: You can use the following commands to interact with the expense tracker:
     **Add an Expense**:
     ```bash
     python expense_tracker.py --add "Food" 200 "2024-12-23"
  **View All Expenses**:
  ```bash
    python expense_tracker.py --view



  
  
    
    
