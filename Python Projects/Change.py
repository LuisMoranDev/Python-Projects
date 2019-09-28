def changeBack():
	cents = {"Quarters: ":.25, "Dimes: ":.10, "Nickels: ":0.05, "Pennies ": 0.01}
	while True:
		try:
			cost = float(input("Enter the cost of the item: "))
		except ValueError:
			print("Cost must be an integer")
		else:
			if cost < 0:
				print("The cost of the item must be greater than 0")
			else:
				break

	while True:
		try:
			money_given = float(input("Enter the amount of money given "))
		except ValueError:
			print("Money given to pay must be an integer")

		else:
			if money_given < cost:
				print("Money given must be equal to or more than cost of item ")
			elif money_given >= cost:
				break
	change = money_given - cost


	for cent in cents:

		if change / cents[cent] > 1:
			a = change / cents[cent]
			change = round(change % cents[cent],2)
			cents[cent] = int(a)

		else:
			cents[cent] = 0
			cents[cent] = int(cents[cent])
	print("Change back will be")
	for x, y in cents.items():
		print(x, y)

changeBack()

# cents = {"Quarters: ":.25, "Dimes: ":.10, "Nickels: ":0.05, "Pennies ": 0.01}

# for x, y in cents.items():
# 	print(x,y)

# left = 1.40 / .25
# change = round(1.40 % .25, 2)
# print(change)

a = .30 
b = .25

# print(round(a % b,2))
