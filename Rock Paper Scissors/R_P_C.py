import random

INTRO = ("""
:'######::::::'###::::'##::::'##:'########:::::'#######::'##::: ##:'####:
'##... ##::::'## ##::: ###::'###: ##.....:::::'##.... ##: ###:: ##: ####:
 ##:::..::::'##:. ##:: ####'####: ##:::::::::: ##:::: ##: ####: ##: ####:
 ##::'####:'##:::. ##: ## ### ##: ######:::::: ##:::: ##: ## ## ##:: ##::
 ##::: ##:: #########: ##. #: ##: ##...::::::: ##:::: ##: ##. ####::..:::
 ##::: ##:: ##.... ##: ##:.:: ##: ##:::::::::: ##:::: ##: ##:. ###:'####:
. ######::: ##:::: ##: ##:::: ##: ########::::. #######:: ##::. ##: ####:
:......::::..:::::..::..:::::..::........::::::.......:::..::::..::....::

""")

DRAW = ("""
.########..########.....###....##......##
.##.....##.##.....##...##.##...##..##..##
.##.....##.##.....##..##...##..##..##..##
.##.....##.########..##.....##.##..##..##
.##.....##.##...##...#########.##..##..##
.##.....##.##....##..##.....##.##..##..##
.########..##.....##.##.....##..###..###.
""")

Rock = 	("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

""")


Paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

""")

Scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

""")

BORDER = ("""
==================================
                VS
==================================
""")


options = {
	"Rock",
	"Paper", 
	"Scissors"
	}
print(INTRO)
while True:
	player_ipt = input("What do you choice? > ")
	com_result = random.choice(list(options))
	
	if player_ipt == com_result:
		print(DRAW)
		print("\nDraw, The Opponent choice " + com_result + " as well")
	elif player_ipt != com_result:

	# Rock VS Paper - Fail!
		if player_ipt == "Rock" and com_result == "Paper":
			print("\nPlayer chose " + player_ipt)
			print(Rock)
			print(BORDER)
			print("Computer chose " + com_result)
			print(Paper)
			print("\nComputer Win! , Player Lose!")
	# Paper VS Rock - Score!
		elif player_ipt == "Paper" and com_result == "Rock":
			print("\nPlayer chose " + player_ipt)
			print(Paper)
			print(BORDER)
			print("\nComputer chose " + com_result)
			print(Rock)
			print("\nPlayer Win! , Computer Lose!")
	# Paper VS Scissors - Fail!
		elif player_ipt == "Paper" and com_result == "Scissors":
			print("\nPlayer chose " + player_ipt)
			print(Paper)
			print(BORDER)
			print("\nComputer chose " + com_result)
			print(Scissors)
			print("\nComputer Win! , Player Lose!")
	# Scissors VS Paper - Score!
		elif player_ipt == "Scissors" and com_result == "Paper":
			print("\nPlayer chose " + player_ipt)
			print(Scissors)
			print(BORDER)
			print("\nComputer chose " + com_result)
			print(Paper)
			print("\nPlayer Win! , Computer Lose!")
	# Scissors VS Rock - Fail!
		elif player_ipt == "Scissors" and com_result == "Rock":
			print("\nPlayer chose " + player_ipt)
			print(Scissors)
			print(BORDER)
			print("\nComputer chose " + com_result)
			print(Rock)
			print("\nComputer Win! , Player Lose!")
	# Rock VS Scissors - Score!
		elif player_ipt == "Rock" and com_result == "Scissors":
			print("\nPlayer chose " + player_ipt)
			print(Rock)
			print(BORDER)
			print("\nComputer chose " + com_result)
			print(Scissors)
			print("\nPlayer Win! , Computer Lose!")
		else:
			print("Please use Scissors,Rock,Paper")
	else:
		print("Error 1 = NANI!")
