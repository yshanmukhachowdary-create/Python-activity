```python
# Multi-Plan Telecommunications Cost Optimization

plans = [
    ["Plan A", 199, 2, 200, 28],
    ["Plan B", 299, 5, 500, 28],
    ["Plan C", 399, 10, 1000, 56],
    ["Plan D", 499, 15, 1500, 84]
]

DATA_RATE = 20
CALL_RATE = 1

# Get user requirements
data_usage = float(input("Enter monthly data usage in GB: "))
call_minutes = int(input("Enter monthly calling minutes: "))
budget = float(input("Enter your budget in Rs.: "))
required_validity = int(input("Enter required validity in days: "))

# Validate inputs
if data_usage < 0 or call_minutes < 0:
    print("Invalid input! Usage cannot be negative.")

elif budget < 0 or required_validity <= 0:
    print("Invalid budget or validity.")

else:
    eligible_plans = []

    print("\n========== PLAN COMPARISON ==========")

    for plan in plans:

        name = plan[0]
        price = plan[1]
        data_limit = plan[2]
        call_limit = plan[3]
        validity = plan[4]

        # Calculate excess charges
        extra_data = max(0, data_usage - data_limit)
        extra_calls = max(0, call_minutes - call_limit)

        data_charge = extra_data * DATA_RATE
        call_charge = extra_calls * CALL_RATE

        total_cost = price + data_charge + call_charge

        print("\nPlan:", name)
        print("Base Price: Rs.", price)
        print("Excess Data Charge: Rs.", round(data_charge, 2))
        print("Excess Calling Charge: Rs.", round(call_charge, 2))
        print("Total Cost: Rs.", round(total_cost, 2))
        print("Validity:", validity, "days")

        # Check eligibility
        if validity >= required_validity and total_cost <= budget:
            eligible_plans.append(
                [name, total_cost, validity, price]
            )
            print("Status: Eligible")

        else:
            print("Status: Not Eligible")

    # Find the most economical eligible plan
    print("\n========== FINAL RESULT ==========")

    if len(eligible_plans) == 0:
        print("No plan satisfies your budget and validity requirements.")

    else:
        eligible_plans.sort(key=lambda x: (x[1], x[2], x[3]))

        best_plan = eligible_plans[0]

        print("Most Economical Plan:", best_plan[0])
        print("Total Cost: Rs.", round(best_plan[1], 2))
        print("Validity:", best_plan[2], "days")

        print("\nOther Eligible Plans:")

        for plan in eligible_plans:
            print(
                plan[0],
                "- Total Cost: Rs.",
                round(plan[1], 2),
                "- Validity:",
                plan[2],
                "days"
            )
```