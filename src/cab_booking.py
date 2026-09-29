def calculate_fare(distance, rate_per_km):
    return distance * rate_per_km


def get_cab_details(cab_type):
    cabs = {
        "Mini": 12,
        "Sedan": 15,
        "SUV": 20
    }

    return cabs.get(cab_type, 0)


if __name__ == "__main__":
    distance = 10
    cab_type = "Sedan"

    rate = get_cab_details(cab_type)
    fare = calculate_fare(distance, rate)

    print("Cab Type:", cab_type)
    print("Distance:", distance, "km")
    print("Estimated Fare: ₹", fare)