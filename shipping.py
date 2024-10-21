def calculate_shipping_cost(weight, distance):
    """
    Calculate shipping cost based on weight and distance.
    
    Basic rate example:
    - $5 flat rate
    - $0.50 per km for weights up to 2kg
    - $1.00 per km for weights between 2kg and 5kg
    - $1.50 per km for weights above 5kg
    """
    base_rate = 5.00  # Flat base rate

    # Determine the rate per km based on the weight
    if weight <= 2:
        rate_per_km = 0.50
    elif weight <= 5:
        rate_per_km = 1.00
    else:
        rate_per_km = 1.50

    # Calculate total shipping cost
    cost = base_rate + (rate_per_km * distance)
    
    return cost

def shipping_calculator():
    print("Welcome to the Shipping Cost Calculator!")
    
    while True:
        try:
            weight = float(input("Enter the weight of the package (in kg): "))
            if weight <= 0:
                print("Weight must be a positive number.")
                continue

            distance = float(input("Enter the shipping distance (in km): "))
            if distance <= 0:
                print("Distance must be a positive number.")
                continue

        except ValueError:
            print("Invalid input! Please enter a numeric value.")
            continue

        cost = calculate_shipping_cost(weight, distance)
        print(f"The shipping cost for a {weight}kg package over {distance}km is: ${cost:.2f}")

        another = input("Would you like to calculate the shipping cost for another package? (y/n): ").lower()
        if another != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    shipping_calculator()

