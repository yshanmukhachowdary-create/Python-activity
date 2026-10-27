```python
# Multi-Currency Travel Budget Analysis

# Sample exchange rates relative to INR
exchange_rates = {
    "INR": 1.0,
    "USD": 85.0,
    "EUR": 95.0
}

conversion_fee_rate = 2
budget = 100000

expenses = []

# Get number of expenses
n = int(input("Enter number of travel expenses: "))

# Process each expense
for i in range(n):

    print("\nExpense", i + 1)

    category = input(
        "Enter category (Accommodation/Food/Transport/Shopping): "
    )

    amount = float(input("Enter expense amount: "))
    currency = input("Enter currency (INR/USD/EUR): ").upper()

    # Validate input
    if amount < 0:
        print("Invalid amount. Expense skipped.")
        continue

    if currency not in exchange_rates:
        print("Unsupported currency. Expense skipped.")
        continue

    # Convert expense into INR
    converted_amount = amount * exchange_rates[currency]

    # Apply conversion fee only to foreign currencies
    if currency != "INR":
        conversion_fee = (
            converted_amount * conversion_fee_rate / 100
        )
    else:
        conversion_fee = 0

    total_expense = converted_amount + conversion_fee

    # Store expense details
    expenses.append([
        category,
        amount,
        currency,
        converted_amount,
        conversion_fee,
        total_expense
    ])

# Calculate total spending by category
category_totals = {}
total_spending = 0

print("\n========== TRAVEL EXPENSE REPORT ==========")

for expense in expenses:

    category = expense[0]
    amount = expense[1]
    currency = expense[2]
    converted = expense[3]
    fee = expense[4]
    total = expense[5]

    print("\nCategory:", category)
    print("Original Expense:", amount, currency)
    print("Converted Amount: Rs.", round(converted, 2))
    print("Conversion Fee: Rs.", round(fee, 2))
    print("Total Expense: Rs.", round(total, 2))

    if category in category_totals:
        category_totals[category] += total
    else:
        category_totals[category] = total

    total_spending += total

# Budget analysis
print("\n========== B")
