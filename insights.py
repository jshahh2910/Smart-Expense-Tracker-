import pandas as pd
import os 

def weekly_spending():
    if not os.path.exists("expenses.csv"):
        print("No expenses found. Add one first.\n")
        return
    spending = pd.read_csv("expenses.csv")
    spending["date"] = pd.to_datetime(spending["date"], dayfirst=True)

    current_week = pd.Timestamp.now().isocalendar().week
    weekly_total = spending[spending["date"].dt.isocalendar().week == current_week]["amount"].sum()

    print(f"\nThis Week's Spending: ₹{weekly_total}\n")


def detect_spending_spike():
    if not os.path.exists("expenses.csv"):
        print("No expenses found. Add one first.\n")
        return
    spending = pd.read_csv("expenses.csv")
    spending["date"] = pd.to_datetime(spending["date"], dayfirst=True)
    current_week = pd.Timestamp.now().isocalendar().week
    current_week_total = spending[spending["date"].dt.isocalendar().week == current_week]["amount"].sum()
    last_week =  current_week - 1
    last_week_total = spending[spending["date"].dt.isocalendar().week == last_week]["amount"].sum()

    if last_week_total == 0:
        if current_week_total == 0:
            print("\nNo spending data available for this week or last week.\n")
        else:
            print(f"\nYou spent ₹{current_week_total} this week. No spending data exists for last week, so a percentage comparison can't be calculated.\n")
        return

    spending_spike = ((current_week_total - last_week_total) / last_week_total) * 100

    if spending_spike > 20:
        print(f"\nYou spent ₹{current_week_total} this week vs ₹{last_week_total} last week — a {spending_spike:.2f}% increase. \n")
    elif spending_spike < 0:
        print(f"\nGood job — your spending is down {abs(spending_spike):.2f}% compared to last week.\n ")
    else:
        print(f"\nYour spending changed by {spending_spike:.2f}% compared to last week.\n")

    

def overspending_category():
    if not os.path.exists("expenses.csv"):
        print("No expenses found. Add one first.\n")
        return
    spending = pd.read_csv("expenses.csv")
    spending["date"] = pd.to_datetime(spending["date"], dayfirst=True)
    today = pd.Timestamp.today()
    current_month_data = spending[(spending["date"].dt.month == today.month) & (spending["date"].dt.year == today.year)]
    last_month = today.month - 1
    last_year = today.year
    if last_month == 0:
        last_month = 12
        last_year -= 1
    last_month_data = spending[(spending["date"].dt.month == last_month) & (spending["date"].dt.year == last_year)]
    current_totals = current_month_data.groupby("category")["amount"].sum()
    last_totals = last_month_data.groupby("category")["amount"].sum()
    if current_totals.empty:
        print("No expenses found for this month.\n")
        return

    top_category = current_totals.idxmax()
    this_month = current_totals[top_category]
    last_month_amount = last_totals.get(top_category, 0)
    difference = this_month - last_month_amount
    print(f"\nTop spending category this month: {top_category}")

    if last_month_amount == 0:
        print(f"You spent ₹{this_month} on {top_category} this month. No spending in this category last month.\n")
    elif difference > 0:
        print(f"You've spent ₹{difference} more on {top_category} than last month.\n")
    elif difference < 0:
        print(f"You've spent ₹{abs(difference)} less on {top_category} than last month.\n")
    else:
        print(f"Your spending on {top_category} is unchanged from last month.\n")


def frequent_purchases():
    if not os.path.exists("expenses.csv"):
        print("No expenses found. Add one first.\n")
        return
    spending = pd.read_csv("expenses.csv")
    spending["date"] = pd.to_datetime(spending["date"], dayfirst=True)
    today = pd.Timestamp.today()
    current_month_data = spending[
        (spending["date"].dt.month == today.month)
        & (spending["date"].dt.year == today.year)
    ]

    if current_month_data.empty:
        print("\nNo expenses found for this month.\n")
        return

    category_totals = current_month_data["category"].value_counts()
    print("\n Most Frequent Purchases This Month: \n")
    for category, value_counts in category_totals.items():
        print(f"{category: <15} {value_counts}")
    print("\n")
