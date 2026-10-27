```python
# Railway Fare and Reservation Calculator

def calculate_fare(distance, travel_class, age):

    # Fare rates per kilometer
    rates = {
        "Sleeper": 1.0,
        "AC3": 2.0,
        "AC2": 3.0
    }

    # Reservation fees
    reservation_fees = {
        "Sleeper": 20,
        "AC3": 40,
        "AC2": 60
    }

    # Distance-based fare
    basic_fare = distance * rates[travel_class]

    # Distance slab charge
    if distance <= 100:
        slab_charge = 50
    elif distance <= 500:
        slab_charge = 100
    else:
        slab_charge = 200

    fare_before_concession = basic_fare + slab_charge

    # Age-based concession
    if age < 5:
        concession_rate = 100
    elif age < 12:
        concession_rate = 50
    elif age >= 60:
        concession_rate = 20
    else:
        concession_rate = 0

    concession = fare_before_concession * concession_rate / 100

    # Reservation fee
    reservation_fee = reservation_fees[travel_class]

    # Final ticket fare
    total_fare = (
        fare_before_concession
        - concession
        + reservation_fee
    )

    return (
        basic_fare,
        slab_charge,
        concession,
        reservation_fee,
        total_fare
    )


def calculate_cancellation_penalty(fare, age, hours_before_departure):

    # Free-travel passengers pay no cancellation penalty
    if age < 5:
        return 0

    # Exclude reservation fee from the penalty calculation
    fare_without_reservation = fare

    if hours_before_departure > 48:
        penalty_rate = 10
    elif hours_before_departure >= 12:
        penalty_rate = 25
    else:
        penalty_rate = 50

    penalty = fare_without_reservation * penalty_rate / 100

    return penalty


# Main program
passengers = []

number = int(input("Enter number of passengers: "))

for i in range(number):

    print("\nPassenger", i + 1)

    name = input("Enter passenger name: ")
    age = int(input("Enter passenger age: "))
    distance = float(input("Enter travel distance in km: "))

    print("Available classes: Sleeper, AC3, AC2")
    travel_class = input("Enter travel class: ")
