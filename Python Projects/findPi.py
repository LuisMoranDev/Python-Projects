import math 

def findPi():

	maxPi = 10

	while True:
		try:
			n = int(input("Please enter the nth number decimal place of pie not going over 10: "))

		except ValueError:
			print("Must be an integer")

		else:
			if n > maxPi: 
				print("Nth number must not be more than 10")
			else:
				break
	pies = str(math.pi)

	print(pies[:n+2])

# findPi()

def sequenceInFib():
	def seq():
		low = 0
		while True:

			try:
				n = int(input("Enter the number of sequences: "))

			except ValueError:
				print("Must be an integer")

			else:
				
				if n < low:
					print("number of sequences must be greater than 0")
				else:
					break 
		a = 1
		b = 1

		for i in range(n):
			yield a
			a,b = b, a+b
	
	def printSeq():
		for number in seq():
			print(number)
	seq()
	printSeq()  

sequenceInFib()




