```python
# Hospital Billing and Patient Classification System

def calculate_bill(consultations, tests, treatment):
    consultation_charge = consultations * 500
    diagnostic_charge = tests * 300

    total_bill = (
        consultation_charge
        + diagnostic_charge
        + treatment
    )

    return consultation_charge, diagnostic_charge, total_bill


# Get patient details
name = input("Enter patient name: ")
age = int(input("Enter patient age: "))

# Validate age
if age < 0:
    print("Invalid age. Age cannot be negative.")

else:
    consultations = int(input("Enter number of consultations: "))
    tests = int(input("Enter number of diagnostic tests: "))
    treatment = float(input("Enter treatment charges: "))

    # Validate billing constraints
    if consultations < 0 or tests < 0 or treatment < 0:
        print("Invalid input! Charges and quantities cannot be negative.")

    else:
        # Calculate charges
        consultation_charge, diagnostic_charge, total_bill = calculate_bill(
            consultations, tests, treatment
        )

        # Apply concessions
        concession_rate = 0

        if age >= 60:
            concession_rate = 10

        if total_bill > 10000 and concession_rate < 5:
            concession_rate = 5

        concession = total_bill * concession_rate / 100
        payable_amount = total_bill - concession

        # Classify patient by payable amount
        if payable_amount <= 5000:
            classification = "Low Payment"

        elif payable_amount <= 15000:
            classification = "Medium Payment"

        else:
            classification = "High Payment"

        # Display hospital bill
        print("\n========== HOSPITAL BILL ==========")
        print("Patient Name:", name)
        print("Patient Age:", age)

        print("\nConsultation Charges: Rs.", consultation_charge)
        print("Diagnostic Charges: Rs.", diagnostic_charge)
        print("Treatment Charges: Rs.", treatment)

        print("-----------------------------------")
        print("Total Bill: Rs.", round(total_bill, 2))
        print("Concession Rate:", concession_rate, "%")
        print("Concession Amount: Rs.", round(concession, 2))
        print("Final Payable Amount: Rs.", round(payable_amount, 2))

        print("\nPatient Classification:", classification)
        print("===================================")
```