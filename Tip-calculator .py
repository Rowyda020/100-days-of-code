#Tip-calculator 👇
print("Welcome to the tip calculator")
bill = float(input("what was your total bil? $"))
tip = int(input("what percentage whould you like to tip? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
new_bill =tip/100*bill+bill
total_bill = float(new_bill/people)
final_cost = round(total_bill,2)
print(f"each person would pay ${final_cost}")
