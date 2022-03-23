#Welcome Mesage
print("Welcome to the Tip Calculator !")

#Taking input from user and coverting it to float for accurate result.
bill = float(input("What was the Total Bill? Rs"))

#Taking input the tip percent from the user and converting into integer.
tip = int(input("What percentage of tip would you like to give? 5, 10, 15 or 20? 'Please provide only number': "))
#Taking input of in how many people the bill will get spilt and converting it to integer.
people = int(input("How many people to split the bill? "))

#Converting tip into percentage.
tip_in_percent = tip / 100

#Multiplying the bill amount with tip_in_percentage to get bill_percent.
bill_percent = tip_in_percent * bill

#Adding the bill_percent with bill to get total amount.
total_bill = bill_percent + bill

#Finding the bill per person by dividing the total bill with people.
bill_per_person = total_bill / people

#Rounding the bill_per_person to two decimal places for exact result.
final_amount = round(bill_per_person, 2)

#Printing the final amount with F-String.
print(f"Each person should pay: Rs{final_amount} ")



