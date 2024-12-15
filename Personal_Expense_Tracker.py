import sqlite3
import datetime
import matplotlib.pyplot as plt
import pandas as pd

def create_database():
    conn = sqlite3.connect('expenses_data.db')
    cursor = conn.cursor()
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY,category TEXT,amount REAL,date TEXT,description TEXT)''')
    conn.commit()
    conn.close()

def add_expense(category, amount, date, description):
    conn = sqlite3.connect('expenses_data.db')
    cursor = conn.cursor()
    cursor.execute(''' 
        INSERT INTO expenses (category, amount, date, description) 
        VALUES (?, ?, ?, ?)
    ''', (category, amount, date, description))
    conn.commit()
    conn.close()

def view_expenses():
    conn = sqlite3.connect('expenses_data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM expenses')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

def monthly_summary():
    current_month = datetime.datetime.now().strftime("%Y-%m")
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT category, SUM(amount) FROM expenses
        WHERE strftime('%Y-%m', date) = ?
        GROUP BY category
    ''', (current_month,))
    summary = cursor.fetchall()
    conn.close()
    return summary

def plot_expenses(data):
    categories = [entry[0] for entry in data]
    amounts = [entry[1] for entry in data]
    plt.figure(figsize=(10, 6))
    plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.title('Spending Breakdown by Category')
    plt.show()

def export_to_excel():
    conn = sqlite3.connect('expenses.db')
    df = pd.read_sql_query("SELECT * FROM expenses", conn)
    df.to_excel('expenses.xlsx', index=False)
    conn.close()

def get_user_input():
    category = input("Enter the expense category (e.g., Groceries, Entertainment, etc.): ")
    amount = float(input("Enter the amount: "))
    date = input("Enter the date of the expense (YYYY-MM-DD): ")
    description = input("Enter a description for the expense: ")
    return category, amount, date, description

def main():
    # Create the database (run once)
    create_database()
    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add an expense")
        print("2. View all expenses")
        print("3. Show monthly summary")
        print("4. Plot spending by category")
        print("5. Export data to Excel")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            category, amount, date, description = get_user_input()
            add_expense(category, amount, date, description)
            print("Expense added successfully!")

        elif choice == '2':
            print("All Expenses:")
            view_expenses()

        elif choice == '3':
            summary = monthly_summary()
            print("\nMonthly Summary:")
            for item in summary:
                print(f"Category: {item[0]}, Total Spending: {item[1]}")

        elif choice == '4':
            summary = monthly_summary()
            print("\nPlotting spending by category...")
            plot_expenses(summary)

        elif choice == '5':
            print("\nExporting data to expenses.xlsx...")
            export_to_excel()

        elif choice == '6':
            print("Exiting the expense tracker...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

