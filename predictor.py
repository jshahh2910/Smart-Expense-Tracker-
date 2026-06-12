import pandas as pd
import os
import calendar


def predict_monthly_expense():
    if not os.path.exists("expenses.csv"):
        print("No expenses found. Add one first.\n")
        return
    spending = pd.read_csv("expenses.csv")
    spending["date"] = pd.to_datetime(spending["date"], dayfirst=True)

    today = pd.Timestamp.today()
    current_month_data = spending[(spending["date"].dt.month == today.month) & (spending["date"].dt.year == today.year)]
    if current_month_data.empty:
        print("No expenses this month to base a prediction on.\n")
        return

    total_spent = current_month_data["amount"].sum()
    current_day = today.day
    days_in_month = calendar.monthrange(today.year, today.month)[1]

    daily_average = total_spent / current_day
    predicted_total = daily_average * days_in_month

    days_left = days_in_month - current_day

    print("\nMonthly Expense Prediction \n")
    print(f"Spent so far      : ₹{total_spent:.2f}")
    print(f"Daily Average     : ₹{daily_average:.2f}")
    print(f"Days Remaining    : {days_left}")
    print(f"Predicted Total   : ₹{predicted_total:.2f}")
    print("\n")
    


def predict_next_month():
    if not os.path.exists("expenses.csv"):
        print("No expense history found.\n")
        return

    spending = pd.read_csv("expenses.csv")
    spending["date"] = pd.to_datetime(spending["date"], dayfirst=True)
    if spending.empty:
        print("No historical data available.\n")
        return

    spending["month"] = spending["date"].dt.to_period("M")
    monthly_totals = (spending.groupby("month")["amount"].sum().sort_index())
    if monthly_totals.empty:
        print("No historical data available.\n")
        return
    
    last_months = monthly_totals.tail(3)
    prediction = last_months.mean()
    print("\nNext Month Prediction \n")
    print("Based on recent spending:\n")
    for month, amount in last_months.items():
        print(f"{month} : ₹{amount:.2f}")

    print("\n")
    print(f"Predicted Next Month Spending : ₹{prediction:.2f}")
    print("\n")