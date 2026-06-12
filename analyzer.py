import pandas as pd
import os 

def all_time_spending():
    if not os.path.exists("expenses.csv"):
        print("No expenses found. Add one first.\n")
        return
    spending = pd.read_csv("expenses.csv")
    total = spending["amount"].sum()
    print(f"\nAll-Time Spending: ₹{total}\n")


def ytd_spending():
    if not os.path.exists("expenses.csv"):
        print("No expenses found. Add one first.\n")
        return
    spending = pd.read_csv("expenses.csv")
    spending["date"] = pd.to_datetime(spending["date"], dayfirst=True)
    current_year = pd.Timestamp.now().year
    ytd_total = spending[spending["date"].dt.year == current_year]["amount"].sum()
    print(f"\nYTD Spending ({current_year}): ₹{ytd_total}\n")


def spending_by_category():
    if not os.path.exists("expenses.csv"):
        print("No expenses found. Add one first.\n")
        return
    spending = pd.read_csv("expenses.csv")
    category_totals = spending.groupby("category")["amount"].sum()
    category_totals.index.name = None
    print("\nCategory-wise Spending: \n")
    for category, amount in category_totals.items():
        print(f"{category:<15} {amount}")
    print("\n")


def monthly_summary():
    if not os.path.exists("expenses.csv"):
        print("No expenses found. Add one first.\n")
        return
    summary = pd.read_csv("expenses.csv")
    summary["date"] = pd.to_datetime(summary["date"], dayfirst=True)
    summary["month"] = summary["date"].dt.to_period("M")
    monthly_totals = summary.groupby("month")["amount"].sum().sort_index()

    print("\nMonthly Summary:\n")
    for month, amount in monthly_totals.items():
        print(f"{month.strftime('%B %Y'):<15} ₹{amount}")
    print()

def average_daily_expense():
    if not os.path.exists("expenses.csv"):
        print("No expenses found. Add one first.\n")
        return
    spending = pd.read_csv("expenses.csv")
    total_spending = spending["amount"].sum()
    unique_days = spending["date"].nunique()
    average = total_spending / unique_days
    print(f"\nAverage Daily Expense: ₹{average:.2f}\n")
    
