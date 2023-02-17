#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")
#Captures the total bill amount.
totalBill = float(input("What was the total bill? $"))
#Captures the tip percentage.
percentageTip = input("What percentage tip would you like to give? 10, 12, or 15? ")
#Calculates the bill percentage to use in the final operation.
tipOnBill = round(float(1+int(percentageTip)/100), 2)
#Captures the numebr of people that need to pay.
numberPeople = int(input("How many people to split the bill? "))
#Calculates the total payment per person.
totalPayPerPerson = round((totalBill/numberPeople) * tipOnBill, 2)
#Prints the final result and formats it to display 2 decimal numbers.
print("Each person should pay: ${:0.2f}".format(totalPayPerPerson))