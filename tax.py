def calculate_tax(income):
    """
    Calculate the tax based on income using a simple progressive tax system.
    """
    tax = 0

    # Tax brackets (example values, you can modify based on your tax system)
    if income <= 10000:
        tax = 0  # No tax on income up to 10,000
    elif income <= 30000:
        tax = (income - 10000) * 0.10  # 10% tax on income between 10,001 and 30,000
    elif income <= 100000:
        tax = (30000 - 10000) * 0.10 + (income - 30000) * 0.20  # 20% on income between 30,001 and 100,000
    else:
        tax = (30000 - 10000) * 0.10 + (100000 - 30000) * 0.20 + (income - 100000) * 0.30  # 30% for income above 100,000

    return tax

def tax_measuring_tool():
    print("Welcome to the Tax Measuring Tool!")
    
    while True:
        try:
            income = float(input("Enter your total income: "))
            if income < 0:
                print("Income cannot be negative! Please enter a valid amount.")
                continue
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
            continue
        
        tax = calculate_tax(income)
        print(f"Based on an income of {income}, your estimated tax is: {tax:.2f}")

        another = input("Would you like to calculate tax for another income? (y/n): ").lower()
        if another != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    tax_measuring_tool()
