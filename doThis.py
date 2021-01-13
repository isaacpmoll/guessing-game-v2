#imports:

import time
import random

#code:
pick = -1101010101010101
name = input("What is your name? ")
print("Well then, " +name+ ", let's play a guessing game!")
time.sleep(1)
mi = int(input("Pick the minimum range: "))
ma = int(input("Pick the maximum range: "))
ran = random.randint(mi, ma)

while pick != ran:
	pick = int(input("Pick a number within the range of " + str(mi) + " and " + str(ma) + ":"))
	if pick > ran:
		print("\nToo high!")
		time.sleep(0.3)
	elif pick < ran:
		print("\nToo low.")
		time.sleep(0.3)
	else:
		print("You got it!")