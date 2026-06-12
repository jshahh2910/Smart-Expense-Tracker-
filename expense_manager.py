import csv
import os
import pandas as pd
import analyzer
import insights
import predictor

def add_expense():
    amount = float(input("Enter an amount: "))
    category = input("category: ")
    description = input("description: ")
    date = input("Enter the date (dd/mm/yyyy): ")
    payment_method = input("Payment method: ")

    file_exists = os.path.exists("expenses.csv")
    
    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Amount", "Category", "Description", "Date", "Payment Method"])
        writer.writerow([amount, category, description, date, payment_method])

    print("Expenses added successfully \n")

def read_expenses():
    if not os.path.exists("expenses.csv"):
        print("No expenses found. Add one first.\n")
        return
    read = pd.read_csv("expenses.csv")
    print(read.to_string())
    print(" ")

def delete_expense():
    if not os.path.exists("expenses.csv"):
        print("No expenses found. Add one first.")
        return
    with open("expenses.csv", "r") as file:
        rows = list(csv.reader(file))

    if len(rows) <= 1:
        print("No expenses to delete.")
        return

    print("\nExpenses:\n")
    print(f"{'No':<4} {'Amount':<10} {'Category':<15} {'Description':<15} {'Date':<12} {'Payment'}")
    print("-" * 75)

    for i, row in enumerate(rows[1:], start=1):
        print(f"{i:<4} {row[0]:<10} {row[1]:<15} {row[2]:<15} {row[3]:<12} {row[4]}")

    try:
        choice = int(input("Enter row number to delete: "))
        if choice < 1 or choice >= len(rows):
            print("Invalid row number.")
            return

        rows.pop(choice) 

        with open("expenses.csv", "w", newline="") as file:
            csv.writer(file).writerows(rows)

        print("Expense deleted successfully.")
        read_expenses()

    except ValueError:
        print("Please enter a valid number.")


while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Exit")
    print("5. Analyze Expenese")
    print("6. Insights")
    print("7. Prediction")
    
    choice = input("Choose: ")
    
    if choice == "1":
        add_expense()
    elif choice == "2":
        read_expenses()
    elif choice == "3":
        delete_expense()
    elif choice == "4":
        break
    elif choice == "5":
        print("1. All-Time Spending")
        print("2. YTD Spending")
        print("3. Spending By Category")
        print("4. Monthly Summary")
        print("5. Daily Average")

        choice = input("Choose: ")

        if choice == "1":
            analyzer.all_time_spending()
        elif choice == "2":
            analyzer.ytd_spending()
        elif choice == "3":
            analyzer.spending_by_category()
        elif choice == "4":
            analyzer.monthly_summary()
        elif choice == "5":
            analyzer.average_daily_expense()
    
    elif choice == "6":
        print("1. Weekly Spendings.")
        print("2. Spending Spike")
        print("3. Overspending Category")
        print("4. Frequent Purchase")

        choice = input("Choose: ")

        if choice == "1":
            insights.weekly_spending()
        elif choice == "2":
            insights.detect_spending_spike()
        elif choice == "3":
            insights.overspending_category()
        elif choice == "4":
            insights.frequent_purchases()

    elif choice == "7":
        print("1. Predict Monthly Expenses.")
        print("2. Predict Next Month")

        choice = input("Choose: ")

        if choice == "1":
            predictor.predict_monthly_expense()
        elif choice == "2":
            predictor.predict_next_month()