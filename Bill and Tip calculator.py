print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $\n"))
tip = int(input("What percentage tip would you like to give? 10 12 15\n "))
people = int(input("How many people to split the bill?\n "))
tip_percent = tip / 100
total_tip = bill * tip_percent
total_bill = bill + total_tip
bill_person = total_bill / people
final_amount = round(bill_person, 2)
print(f"Each person should pay : {final_amount}")