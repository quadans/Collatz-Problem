def collatz(number):
	if (number % 2) == 0:
		return number//2

	else:	
		return 3 * number + 1

while True:
	print("write a number : ")
	try:
		bla = collatz(int(input()))
		break
	except ValueError:
		print("Du musst eine Zahl eingeben!")
		continue
print(bla)
