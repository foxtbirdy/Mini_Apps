import random

options = {
	"Rock",
	"Paper",
	"Scissors"
	}

while True:
	player_ipt = input("What do you choice? > ")


	com_result = random.choice(list(options))

	if player_ipt == com_result:
		print("Draw, The Opponent choice " + com_result + " as well")
	elif player_ipt != com_result:

	# Rock VS Paper
		if player_ipt == "Rock" and com_result == "Paper":
			print("Failed! The Opponent scored " + com_result)
	# Paper VS Rock
		elif player_ipt == "Paper" and com_result == "Rock":
			print("Scored! The Opponent scored " + com_result)
	# Paper VS Scissors
		elif player_ipt == "Paper" and com_result == "Scissors":
			print("Failed! The Opponent scored " + com_result)
	# Scissors VS Paper
		elif player_ipt == "Scissors" and com_result == "Paper":
			print("Scored! The Opponent scored " + com_result)	
	# Scissors VS Rock 
		elif player_ipt == "Scissors" and com_result == "Rock":
			print("Failed! The Opponent scored " + com_result)
	# Rock VS Scissors 
		elif player_ipt == "Rock" and com_result == "Scissors":
			print("Scored! The Opponent scored " + com_result)

		else:
			print("Error 2")
	else:
		print("Error 1")