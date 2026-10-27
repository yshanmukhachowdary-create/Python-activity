```python
import math

print("===== CAMPUS EVENT FINANCIAL PLANNING =====")

# Input fixed expenses
venue_cost = float(input("Enter venue cost (Rs.): "))
equipment_cost = float(input("Enter equipment cost (Rs.): "))

# Input variable expenses per participant
catering_per_person = float(input("Enter catering cost per participant (Rs.): "))
transport_per_person = float(input("Enter transport cost per participant (Rs.): "))
certificate_per_person = float(input("Enter certificate cost per participant (Rs.): "))

# Input event details
participants = int(input("Enter expected number of participants: "))
sponsorship = float(input("Enter expected sponsorship amount (Rs.): "))
registration_fee = float(input("Enter registration fee per participant (Rs.): "))

# Validate inputs
if (venue_cost < 0 or equipment_cost < 0 or
        catering_per_person < 0 or transport_per_person < 0 or
        certificate_per_person < 0 or participants < 0 or
        sponsorship < 0 or registration_fee < 0):
    print("Error: Costs, participants, sponsorship, and fee cannot be negative.")

else:
    # Calculate fixed and variable costs
    fixed_cost = venue_cost + equipment_cost

    variable_cost_per_person = (
        catering_per_person
        + transport_per_person
        + certificate_per_person
    )

    # Calculate total expenses
    variable_cost = variable_cost_per_person * participants
    total_cost = fixed_cost + variable_cost

    # Calculate participant contributions
    participant_contribution = registration_fee * participants

    # Calculate total available funds
    total_funds = participant_contribution + sponsorship

    # Calculate sponsorship shortfall
    sponsorship_shortfall = max(0, total_cost - sponsorship)

    # Calculate overall budget balance
    balance = total_funds - total_cost

    # Display expense details
    print("\n===== EXPENSE DETAILS =====")
    print(f"Venue Cost: Rs. {venue_cost:.2f}")
    print(f"Equipment Cost: Rs. {equipment_cost:.2f}")
    print(f"Catering Cost: Rs. {catering_per_person * participants:.2f}")
    print(f"Transport Cost: Rs. {transport_per_person * participants:.2f}")
    print(f"Certificate Cost: Rs. {certificate_per_person * participants:.2f}")
    print(f"Total Event Cost: Rs. {total_cost:.2f}")

    print("\n===== FUNDING DETAILS =====")
    print(f"Participant Contributions: Rs. {participant_contribution:.2f}")
    print(f"Expected Sponsorship: Rs. {sponsorship:.2f}")
    print(f"Total Available Funds: Rs. {total_funds:.2f}")
    print(f"Sponsorship Funding Shortfall: Rs. {sponsorship_shortfall:.2f}")

    if balance > 0:
        print(f"Budget Surplus: Rs. {balance:.2f}")
    elif balance < 0:
        print(f"Budget Deficit: Rs. {-balance:.2f}")
    else:
        print("The event budget is exactly balanced.")

    # Calculate minimum registrations required to break even
    contribution_per_person = registration_fee - variable_cost_per_person
    amount_to_recover = fixed_cost - sponsorship

    print("\n===== BREAK-EVEN ANALYSIS =====")

    if amount_to_recover <= 0:
        print("Sponsorship covers all fixed costs.")
        print("Minimum registrations required: 0")

    elif contribution_per_person <= 0:
        print("Break-even is not possible with the current registration fee.")
        print("The fee must be greater than the variable cost per participant.")

    else:
        minimum_registrations = math.ceil(
            amount_to_recover / contribution_per_person
        )

        print(
            "Minimum registrations required:",
            minimum_registrations
        )

        if participants >= minimum_registrations:
            print("Expected registrations are sufficient to break even.")
        else:
            print("More registrations are needed to break even.")
```