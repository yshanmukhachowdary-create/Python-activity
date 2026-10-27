```python
# Progressive Electricity Billing System

def calculate_bill(units):

    # Calculate progressive energy charges
    if units <= 100:
        energy_charge = units * 2

    elif units <= 200:
        energy_charge = (100 * 2) + (units - 100) * 3

    elif units <= 300:
        energy_charge = (100 * 2) + (100 * 3) + (units - 200) * 5

    else:
        energy_charge = (
            (100 * 2)
            + (100 * 3)
            + (100 * 5)
            + (units - 300) * 7
        )

    # Fixed monthly charge
    fixed_charge = 100

    # Calculate surcharge
    surcharge = 0

    if units > 300:
        surcharge = energy_charge * 0.10

    # Calculate rebate
    rebate = 0

    if units < 100:
        rebate = energy_charge * 0.05

    # Calculate total bill
    total_bill = (
        energy_charge
        + fixed_charge
        + surcharge
        - rebate
    )

    return energy_charge, fixed_charge, surcharge, rebate, total_bill


# Main program
months = int(input("Enter number of months: "))

month_names = []
consumptions = []
bills = []

for i in range(months):

    print("\nMonth", i + 1)

    month = input("Enter month name: ")
    units = float(input("Enter electricity consumption in units: "))

    if units < 0:
        print("Invalid consumption. Enter a non-negative value.")
        continue

    energy, fixed, surcharge, rebate, total = calculate_bill(units)

    month_names.append(month)
    consumptions.append(units)
    bills.append(total)

    print("\nElectricity Bill")
    print("-------------------------")
    print("Month:", month)
    print("Units Consumed:", units)
    print("Energy Charges: Rs.", round(energy, 2))
    print("Fixed Charges: Rs.", round(fixed, 2))
    print("Surcharge: Rs.", round(surcharge, 2))
    print("Rebate: Rs.", round(rebate, 2))
    print("Total Bill: Rs.", round(total, 2))


# Compare monthly bills
print("\n========== MONTHLY BILL COMPARISON ==========")

for i in range(len(bills)):

    print(
        month_names[i],
        "- Units:", consumptions[i],
        "- Bill: Rs.", round(bills[i], 2)
    )

    if i > 0:

        increase = bills[i] - bills[i - 1]

        if bills[i - 1] > 0:
            percentage_increase = (
                increase / bills[i - 1]
            ) * 100
        else:
            percentage_increase = 0

        if percentage_increase > 30:
            print("WARNING: Unusual bill increase detected!")

        if increase > 0:
            print("Bill increased by Rs.", round(increase, 2))

        elif increase < 0:
            print("Bill decreased by Rs.", round(abs(increase), 2))
