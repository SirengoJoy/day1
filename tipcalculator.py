meal = float(input("Enter your meal amount: "))
tip = int(input("Enter your tip percentage: "))
tax = .06

tip_amt = meal * tip/100
tax_amt = meal * tax
total = meal + tip_amt + tax_amt

print(f"Your meal was Ksh{meal:.2f} and your tip was Ksh{tip_amt:.2f}")
print(f"Your total amount is: Ksh{total:.2f}")