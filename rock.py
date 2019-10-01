# Naima Ontiveros
# Rock Paper Scissors
#VAIRABLES
import random

pScore = 0
cScore = 0
ties = 0
computerChoices = ["r", "p","s"]


# Welcome message
#	PRINT THE message
print(" Welcome to Rock Paper Scissors ")
# PROMPT FOR PLAYER NAME	
pName =input("What is your name? ")

# Final Score
def printScore():
	print("The score is ")
	# Write message
	print(pName + ": "  + str(pScore))
	# Write player score
	print("Computer: " + str(cScore))
	# Write computer score
	print("Ties "+ str(ties))
	# Write how many ties

#Game loop
# Make a forever loop
while True:
	# Print current score
	printScore()
	# prompt for a choice( r(rock), p(paper), s(scissors), q(quit))
	pChoice = input("Enter  r(rock), p (paper), s (scissors), or q (quit) to quit ")
	# deal with player entering q
	if pChoice == "q":
		break
	# get computers choice (random)
	cChoice = random.choice(computerChoices)

	# compare for player entering r
	if cChoice == "r":
		print(pName + " picked rock")
		if cChoice == "r":
			print("Computer picked Rock")
			print("This is a tie")
			ties = ties + 1
		# if computer is r
		elif cChoice == "p":
			print("Computer picked paper")
			print("Paper cover rock")
			cScore = cScore + 1
		# if computer is p
		else:
			print("Computer picked scissors")
			print("Rock beats scissors")
			pScore = pScore + 1
		# if computer is s
	
	# compare for player entering p
	elif pChoice == "p":
		print(pName + " Picked Paper")
		if cChoice == "r":
			print("Computer picked Rock")
			print("Paper covers rock")
			pScore = pScore +1
		# if computer is r
		elif cChoice == "p":
			print("Computer picked paper")
			print("This is a Tie")
			ties = ties +1
		# if computer is p
		else:
			print("Computer picked scissors")
			print("Scissors beats rock")
			cScore = cScore + 1
		# if computer is s
	# compare for player entering s
	elif pChoice == "s":
		print(pName + " Picked scissors")
		if cChoice == "r":
			print("Computer picked Rock")
			print("Rock beats Scissors")
			cScore = Cscore + 1
		# if computer is r
		elif cChoice == "p":
			print("Computer picked paper")
			print("Scissors beats paper")
			pScore = pScore + 1

		# if computer is p
		else:
			print("Computer picked scissors")
			print("This is a tie oof")
			ties = ties + 1
		# if computer is s
		

		


	# deal with player entering anything else

