# for calculating the specific gravity of soil.

def calculate(water_weight, dry_weight):
    
    try:
        sg = dry_weight / (dry_weight - water_weight)
    except ZeroDivisionError:
        return " Invalid input: dry weight and water weight are too close."
    return round(sg, 3)

# allows to run the code directly from terminal
if __name__ == "__main__":
    water_weight = float(input("Enter water weight (g): "))
    dry_weight = float(input("Enter dry soil weight (g): "))
    result = calculate(water_weight, dry_weight)
    print("✅ Specific Gravity =", result)
