# python_projects

**Personal Expense Tracker: Managing Finances Efficiently for Students**

Managing personal finances can be challenging for students, especially when balancing multiple expenses like rent, food, transportation, and entertainment. Often, students lack the tools or knowledge to track their spending effectively, leading to overspending or financial stress. This Personal Expense Tracker aims to address these issues by providing a user-friendly solution to record, categorize, and analyze expenses.

### Problem
Students often face financial challenges due to limited income and frequent expenses. Without an organized system, it can be hard to keep track of spending, and overspending in certain categories like entertainment or food may occur. Additionally, not knowing where their money is going makes it difficult to budget for future needs. The need for an efficient, easy-to-use tool to monitor finances becomes essential for better financial management.

### Solution
The Personal Expense Tracker is designed to help students easily record and monitor their expenses in real-time. It allows them to categorize their spending and provides visual insights into their financial habits.

### Features:
1. **Expense Entry**: The tracker allows users to input expenses, including the category (e.g., Groceries, Entertainment), the amount spent, the date of the expense, and a brief description.
   
2. **Database Management**: The expenses are stored in an SQLite database, ensuring efficient data storage and retrieval. This makes it easy to manage and update expenses.

3. **Monthly Summary**: The program automatically calculates the total amount spent per category each month. Users can see how much they’ve spent on various categories like food, transportation, and entertainment in a given month.

4. **Visual Representation**: Users can generate pie charts that visually represent their spending distribution by category, helping them understand which areas they may want to cut back on.

5. **Excel Export**: All expenses can be exported to an Excel file for further analysis or record-keeping. This feature makes it easy for users to share their financial data with others or use it for budgeting purposes.

6. **User Input**: The program provides a simple interface where users can enter new expenses through interactive prompts. It guides them through entering categories, amounts, and other necessary details.

7. **Financial Awareness**: By tracking spending trends over time, users gain awareness of their financial habits and can make better decisions to reduce unnecessary expenses.

8. **Simple and Efficient**: The tracker is lightweight, user-friendly, and can be run from the terminal. It requires no prior technical knowledge, making it perfect for students who are not financially savvy.

9. **Time-Saving**: The system streamlines the process of managing finances, making it easier for students to balance their finances without spending hours organizing receipts or bills manually.

### Technologies Used:
- **SQLite**: For storing expenses in a local database.
- **Matplotlib**: For visualizing spending data through pie charts.
- **Pandas**: For handling and exporting data to Excel.

### Key Benefits:
- **Efficient Expense Tracking**: Students can monitor their spending across various categories without having to manually track every purchase.
- **Budget Planning**: The monthly summary and visual charts help students spot trends, making it easier to plan future budgets.
- **Data Export**: Students can easily export their expenses to Excel for further analysis or sharing.
- **User-Friendly**: Designed with simplicity in mind, this tool can be used by anyone, regardless of their technical expertise.

---------------------------------------------------------------------------------------------------------------------------------------------------------


# Grocery Management System

This is a simple Grocery Management System developed in Python to manage products, track inventory, and process customer orders. The system uses CSV files to store product and order information, ensuring data persistence across sessions.

## Features

1. **Product Management**: 
   - Add new products to the inventory.
   - Update product details (name, quantity, price, category, and supplier).
   - Delete products from the inventory.

2. **Order Management**:
   - View all products available for sale.
   - Place orders for products and update stock accordingly.
   - Track order details such as product name, quantity, and total price.

3. **Data Persistence**: 
   - Products and orders are saved in `grocery_products.csv` and `grocery_orders.csv` files.
   - The system loads and saves data from CSV files, ensuring data is retained across program executions.

## Technologies Used
- **Python**: Main programming language.
- **CSV**: For storing and loading product and order data.
- **OOP (Object-Oriented Programming)**: The system is designed using object-oriented principles, utilizing classes like `Product` and `Order`.

## Files
- `grocery_products.csv`: Contains product information such as ID, name, quantity, price, category, and supplier.
- `grocery_orders.csv`: Contains order details like order ID, product ID, quantity, and total price.

## How to Run
1. Clone or download this repository to your local machine.
2. Make sure Python is installed on your system.
3. Run the script using the following command:
   ```bash
   python grocery_management_system.py
   ```

## Example Usage

1. **Add Product**: 
   - Enter product details (name, quantity, price, category, supplier).
2. **Place Order**: 
   - View available products and order a product by specifying quantity.

## Contribution

Feel free to fork this project and submit issues or pull requests to improve the system. Any contributions are welcome!

## License
This project is licensed under the MIT License.

---

This description provides a comprehensive overview of your project and how others can interact with it. You can update it further based on any additional features or changes you make.

