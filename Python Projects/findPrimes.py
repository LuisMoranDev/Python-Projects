def findPrime(n):
	prime = [2,3,5,7,11] 
	numlist = []
	if n < 3:
		print ("No prime number")

	for num in prime:
		while True:
			if n % num == 0:
				n = n / num
				numlist.append(num)
			else:
				break
	print(numlist)

findPrime(2000)
