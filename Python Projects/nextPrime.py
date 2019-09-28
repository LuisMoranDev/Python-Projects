def nextPrimeNum():
	number = 3
	print("2")
	answer = input("Do you want the next prime number?")
	while answer.lower() != "n": 
		if number > 10:
			if number % 2 != 0 and number % 3 != 0 and number % 5 != 0 and number % 7 != 0 and number % 11 != 0:
				print(number)
				answer = input("Do you want the next prime number?")
		elif number % 2 != 0 and number % 1 == 0 and number % number == 0:
			print(number)
			answer = input("Do you want the next prime number?")
		number += 1
	

nextPrimeNum()

