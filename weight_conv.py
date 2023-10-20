weight = float(input("Enter your weight: "))
unit = input("Kilograms or pounds? (K or L): ")

if unit == "K":
    weight = weight * 2.2
    unit ="Lbs"
    print(f"Your weight is: {weight} {unit}")
else:
    print(f"{unit} was not valid")
