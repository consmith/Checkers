
import math

#Initializing the board globally

checkerboard = [[" "]*9 for unused in range(9)]

def playerMovement(player):

	(xPos,yPos,xNewPos,yNewPos) = logicAndCalc(player)

	#Assigning the function to a variable, so that it doesn't need to be run twice
	#if it fails the first 'if'

	(checkedvalue,jumper) = checkLegal(xPos,yPos,xNewPos,yNewPos,player)

	if checkedvalue == True:
		if jumper == True:
			while jumper == True:
				checkerboard[int(yNewPos)][int(xNewPos)] = checkerboard[int(yPos)][int(xPos)]
				checkerboard[int(yPos)][int(xPos)] = " "
				#Above is just moving the piece
				#The jumped piece is deleted in checkLegal
				yPos = yNewPos
				xPos = xNewPos
				xNewPos = xPos - 2, xPos + 2
				yNewPos = yPos - 2, yPos + 2

				#data validation
				#The most that can ever be true at once will only be one, so it
				#should not be a problem exchanging these values.
				if xNewPos[1] > 8:
					xNewPos = xNewPos[0],0
				if yNewPos[1] > 8:
					yNewPos = yNewPos[0],0
				if xNewPos[0] < 0:
					xNewPos = 0,xNewPos[1]
				if yNewPos[0] < 0:
					yNewPos = 0,yNewPos[1]



				#Needs to find if it has any possible jumps

				jumperLocal = checkJump(xPos,yPos,xNewPos,yNewPos,player)

				if jumperLocal == True:
					jumper = False
					checkedvalue = False
					while jumper == False:
						while checkedvalue == False:

							print('\n You can jump again!\n')

							printBoard()

							(xNewPos,yNewPos) = DoubleJumpFunction(player)

							(checkedvalue,jumper) = checkLegal(xPos,yPos,xNewPos,yNewPos,player)
				else:
					jumper = False

		else:

			#Normal Piece Movement
			checkerboard[int(yNewPos)][int(xNewPos)] = checkerboard[int(yPos)][int(xPos)]
			checkerboard[int(yPos)][int(xPos)] = " "
			yPos = yNewPos
			xPos = xNewPos

		if kingMe(yPos,player) == True:

			#Finding who the player is and kinging them

			if player == 1:
				checkerboard[int(yPos)][int(xPos)] = "W"
			else:
				checkerboard[int(yPos)][int(xPos)] = "B"
	else:
		while checkedvalue == False:

			(xPos,yPos,xNewPos,yNewPos) = logicAndCalc(player)

			#Assigning the function to a variable, so that it doesn't need to be run twice
			#if it fails the first 'if'

			(checkedvalue,jumper) = checkLegal(xPos,yPos,xNewPos,yNewPos,player)
			#Everything Above this is a duplicate of the code above
		#Now just duplicating the code of checking the jump and king

		if jumper == True:
			while jumper == True:
				checkerboard[int(yNewPos)][int(xNewPos)] = checkerboard[int(yPos)][int(xPos)]
				checkerboard[int(yPos)][int(xPos)] = " "
				#Above is just moving the piece
				#The jumped piece is deleted in checkLegal
				yPos = yNewPos
				xPos = xNewPos
				xNewPos = xPos - 2, xPos + 2
				yNewPos = yPos - 2, yPos + 2

				#data validation
				if xNewPos[1] > 8:
					xNewPos = xNewPos[0],xNewPos[0]
				if yNewPos[1] > 8:
					yNewPos = yNewPos[0],yNewPos[0]
				if xNewPos[0] < 0:
					xNewPos = xNewPos[1],xNewPos[1]
				if yNewPos[0] < 0:
					yNewPos = yNewPos[1],yNewPos[1]

				#Needs to find if it has any possible jumps

				jumperinitial = checkJump(xPos,yPos,xNewPos,yNewPos,player)

				if jumperinitial == True:
					jumper = False
					checkedvalue = False
					while jumper == False:
						while checkedvalue == False:

							print('\n You can jump again!\n')

							printBoard()

							(xNewPos,yNewPos) = DoubleJumpFunction(player)

							(checkedvalue,jumper) = checkLegal(xPos,yPos,xNewPos,yNewPos,player)
				else:
					jumper = False

		else:

			#Normal Piece Movement
			checkerboard[int(yNewPos)][int(xNewPos)] = checkerboard[int(yPos)][int(xPos)]
			checkerboard[int(yPos)][int(xPos)] = " "
			yPos = yNewPos
			xPos = xNewPos

		if kingMe(yPos,player) == True:

			#Finding who the player is and kinging them

			if player == 1:
				checkerboard[int(yPos)][int(xPos)] = "W"
			else:
				checkerboard[int(yPos)][int(xPos)] = "B"

def logicAndCalc(player):

	LetterPossibilities = "A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h"
	NumberPossibilities = "1","2","3","4","5","6","7","8"

	# Taking the original piece position

	piecePosition = raw_input('\nWhat piece would you like to move? (ex: A2 or a2) player{0}: '.format(player))

	#data validation

	if piecePosition == "quit":
		print('\nSee ya!\n')
		quit()

	if len(piecePosition) != 2 :
		piecePosition = "zz"

	if (LetterPossibilities.count(piecePosition[0]) == 0 or
		NumberPossibilities.count(piecePosition[1]) == 0):
		print("\nThe inputted value is not a piece/allowed.")
		while (LetterPossibilities.count(piecePosition[0]) == 0 or
			NumberPossibilities.count(piecePosition[1]) == 0):
			piecePosition = raw_input('\nWhat piece would you like to move? (ex: A2 or a2) player{0}: '.format(player))
			if piecePosition == "quit":
				print('\nSee ya!\n')
				quit()
			if len(piecePosition) != 2:
				piecePosition = "zz"
			if (LetterPossibilities.count(piecePosition[0]) == 0 or
				NumberPossibilities.count(piecePosition[1]) == 0):
				print("\nThe inputted value is not a piece/allowed.")

	# Choosing where to move the piece

	piecePlacement = raw_input('\nWhere would you like to place this piece? (ex: A2 or a2)\n(you can only move 1 jump or space at a time) player{0}: '.format(player))

	#data validation

	if piecePlacement == "quit":
		print('\nSee ya!\n')
		quit()

	if len(piecePlacement) != 2:
		piecePlacement = "zz"

	if (LetterPossibilities.count(piecePlacement[0]) == 0 or
		NumberPossibilities.count(piecePlacement[1]) == 0):
		print("\nThe inputted value is not a piece/allowed.")
		while (LetterPossibilities.count(piecePlacement[0]) == 0 or
			NumberPossibilities.count(piecePlacement[1]) == 0):
			piecePlacement = raw_input('\nWhere would you like to place this piece? (ex: A2 or a2)\n(you can only move 1 jump or space at a time) player{0}: '.format(player))
			if piecePlacement == "quit":
				print('\nSee ya!\n')
				quit()
			if len(piecePlacement) != 2:
				piecePlacement = "zz"
			if (LetterPossibilities.count(piecePlacement[0]) == 0 or
				NumberPossibilities.count(piecePlacement[1]) == 0):
				print("\nThe inputted value is not a piece/allowed.")

	# Finding old and new position Locations

	for xIndex in range(0,16):
		if piecePosition[0] == LetterPossibilities[xIndex]:
			xPos = math.ceil((xIndex + 1)/2)
		if piecePlacement[0] == LetterPossibilities[xIndex]:
			xNewPos = math.ceil((xIndex + 1)/2)

	for yIndex in range(0,8):
		if piecePosition[1] == NumberPossibilities[yIndex]:
			yPos = yIndex + 1
		if piecePlacement[1] == NumberPossibilities[yIndex]:
			yNewPos = yIndex + 1

	return (xPos,yPos,xNewPos,yNewPos)

def DoubleJumpFunction(player):

	LetterPossibilities = "A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h"
	NumberPossibilities = "1","2","3","4","5","6","7","8"

	piecePlacement = raw_input('\nWhere would you like to place this piece? (ex: A2 or a2)\n(you can only move 1 jump or space at a time) player{0}: '.format(player))

	#data validation

	if piecePlacement == "quit":
		print('\nSee ya!\n')
		quit()

	if len(piecePlacement) != 2:
		piecePlacement = "zz"

	if (LetterPossibilities.count(piecePlacement[0]) == 0 or
		NumberPossibilities.count(piecePlacement[1]) == 0):
		print("\nThe inputted value is not a piece/allowed.")
		while (LetterPossibilities.count(piecePlacement[0]) == 0 or
			NumberPossibilities.count(piecePlacement[1]) == 0):
			piecePlacement = raw_input('\nWhere would you like to place this piece? (ex: A2 or a2)\n(you can only move 1 jump or space at a time) player{0}: '.format(player))
			if piecePlacement == "quit":
				print('\nSee ya!\n')
				quit()
			if len(piecePlacement) != 2:
				piecePlacement = "zz"
			if (LetterPossibilities.count(piecePlacement[0]) == 0 or
				NumberPossibilities.count(piecePlacement[1]) == 0):
				print("\nThe inputted value is not a piece/allowed.")

	# Finding old and new position Locations

	for xIndex in range(0,16):
		if piecePlacement[0] == LetterPossibilities[xIndex]:
			xNewPos = math.ceil((xIndex + 1)/2)

	for yIndex in range(0,8):
		if piecePlacement[1] == NumberPossibilities[yIndex]:
			yNewPos = yIndex + 1

	return (xNewPos,yNewPos)

def checkLegal(xPos,yPos,xNewPos,yNewPos,player):
	xDistance = xNewPos - xPos
	yDistance = yNewPos - yPos
	yAdded = yNewPos + yPos
	xAdded = xNewPos + xPos
	possiblePieces = "w","W","b","B"
	totalPosDis = (abs(xDistance) + abs(yDistance))
	halfDistance = checkerboard[int(yAdded/2)][int(xAdded/2)]
	jumper = False
	#Checking that the piece chosen is the player's own piece

	if player == 1:
		if (checkerboard[int(yPos)][int(xPos)] == "b" or
			checkerboard[int(yPos)][int(xPos)] == "B"):
			print('\n The chosen piece must be your own')
			return False,jumper
		elif checkerboard[int(yPos)][int(xPos)] == "w":
			if yDistance > 0:
				print('\nthe chosen piece cannot move backwards because it is not a king')
				return False,jumper

	elif player == 2:
		if (checkerboard[int(yPos)][int(xPos)] == "w" or
			checkerboard[int(yPos)][int(xPos)] ==  "W"):
			print('\n The chosen piece must be your own')
			return False,jumper
		elif checkerboard[int(yPos)][int(xPos)] == "b":
			if yDistance < 0:
				print('\nthe chosen piece cannot move backwards because it is not a king')
				return False,jumper

	#Checking correct tile, non-empty chosen spot, legal jump(if jumping), and correct distance
	#in the order that it was listed here

	if totalPosDis % 2 != 0 :
		print('\nyou can not move to this space')
		return False,jumper
	elif possiblePieces.count(checkerboard[int(yPos)][int(xPos)]) == 0:
		print('\nthe chosen spot was empty')
		return False,jumper
	elif possiblePieces.count(checkerboard[int(yNewPos)][int(xNewPos)]) > 0 :
		print('\nThere is a piece already where you want to move!')
		return False,jumper
	elif totalPosDis == 4 :
		if player == 1 :
			if xDistance == 0 or yDistance == 0 :
				print('\nDouble jumps must be performed by 2 separate jumps')
				return False,jumper
			elif halfDistance != "b" :
				if halfDistance != "B" :
					print('\nEither there is no piece between you and your chosen spot or you can not jump over your own piece')
					return False,jumper
				else:
					jumper = True
					checkerboard[int(math.ceil(yAdded/2))][int(math.ceil(xAdded/2))] = " "
					return (True,jumper)
			else:
				jumper = True
				checkerboard[int(math.ceil(yAdded/2))][int(math.ceil(xAdded/2))] = " "
				return (True,jumper)
		elif player == 2 :
			if xDistance == 0 or yDistance == 0 :
				print('\nDouble jumps must be performed by 2 separate jumps')
				return False,jumper
			elif halfDistance != "w" :
				if halfDistance != "W" :
					print('\nEither there is no piece between you and your chosen spot or you can not jump over your own piece')
					return False,jumper
				else:
					jumper = True
					checkerboard[int(math.ceil(yAdded/2))][int(math.ceil(xAdded/2))] = " "
					return (True,jumper)
			else:
				jumper = True
				checkerboard[int(math.ceil(yAdded/2))][int(math.ceil(xAdded/2))] = " "
				return (True, jumper)
		else:
			pass
	elif totalPosDis > 4:
		print('\nThis move was too far. Remember, jumps must be performed one at a time.')
		return False,jumper
	else:
		return True,jumper

def checkJump(xPos,yPos,xNewPos,yNewPos,player):

	yAdded = (yNewPos[0] + yPos,yNewPos[1] + yPos)
	xAdded = (xNewPos[0] + xPos,xNewPos[1] + xPos)
	halfDistance = (checkerboard[int(yAdded[0]/2)][int(xAdded[0]/2)],#Both Negative [0][0] = [0]
					checkerboard[int(yAdded[0]/2)][int(xAdded[1]/2)],#y neg, x pos  [0][1] = [1]
					checkerboard[int(yAdded[1]/2)][int(xAdded[0]/2)],#y pos, x neg, [1][0] = [2]
					checkerboard[int(yAdded[1]/2)][int(xAdded[1]/2)])#Both pos      [1][1] = [3]
	jumperLocal = False


	if player == 1:
		if checkerboard[int(yPos)][int(xPos)] == 'w':
			if checkerboard[int(yNewPos[0])][int(xNewPos[0])] == " ":
				if halfDistance[0] == "b" or halfDistance[0] == "B" :
					jumperLocal = True
			if checkerboard[int(yNewPos[0])][int(xNewPos[1])] == " ":
				if halfDistance[1] == "b" or halfDistance[1] == "B" :
					jumperLocal = True
		else:
			if checkerboard[int(yNewPos[0])][int(xNewPos[0])] == " ":
				if halfDistance[0] == "b" or halfDistance[0] == "B" :
					jumperLocal = True
			if checkerboard[int(yNewPos[0])][int(xNewPos[1])] == " ":
				if halfDistance[1] == "b" or halfDistance[1] == "B" :
					jumperLocal = True
			if checkerboard[int(yNewPos[1])][int(xNewPos[0])] == " ":
				if halfDistance[2] == "b" or halfDistance[2] == "B" :
					jumperLocal = True
			if checkerboard[int(yNewPos[1])][int(xNewPos[1])] == " ":
				if halfDistance[3] == "b" or halfDistance[3] == "B" :
					jumperLocal = True

	elif player == 2:
		if checkerboard[int(yPos)][int(xPos)] == 'b':
			if checkerboard[int(yNewPos[1])][int(xNewPos[0])] == " ":
				if halfDistance[2] == "w" or halfDistance[2] == "W" :
					jumperLocal = True
			if checkerboard[int(yNewPos[1])][int(xNewPos[1])] == " ":
				if halfDistance[3] == "w" or halfDistance[3] == "W" :
					jumperLocal = True
		else:
			if checkerboard[int(yNewPos[0])][int(xNewPos[0])] == " ":
				if halfDistance[0] == "w" or halfDistance[0] == "W" :
					jumperLocal = True
			if checkerboard[int(yNewPos[0])][int(xNewPos[1])] == " ":
				if halfDistance[1] == "w" or halfDistance[1] == "W" :
					jumperLocal = True
			if checkerboard[int(yNewPos[1])][int(xNewPos[0])] == " ":
				if halfDistance[2] == "w" or halfDistance[2] == "W" :
					jumperLocal = True
			if checkerboard[int(yNewPos[1])][int(xNewPos[1])] == " ":
				if halfDistance[3] == "w" or halfDistance[3] == "W" :
					jumperLocal = True

	return jumperLocal

def checkWin():


	player1win = True
	player2win = True
	for x in range(1,9):
		for y in range(1,9):
			if checkerboard[y][x] == "b" or checkerboard[x][y] == "B":
				player1win = False
			if checkerboard[y][x] == "w" or checkerboard[x][y] == "W":
				player2win = False

	if player1win == True:
		print('\nPlayer1 has won!\n')
		return True
	elif player2win == True:
		print('\nPlayer2 has won!\n')
		return True
	else:
		return False

def kingMe(yNewPos,player):

	#Checking for player, then if player is in the appropriate kinging spot

	if player == 1:
		if yNewPos == 1:
			return True
		else:
			return False
	else:
		if yNewPos == 8:
			return True
		else:
			return False

def initBoard():

	#This is just assigning the outer values

	checkerboard[0][0:8]="~","A","B","C","D","E","F","G","H"
	checkerboard[1][0]="1"
	checkerboard[2][0]="2"
	checkerboard[3][0]="3"
	checkerboard[4][0]="4"
	checkerboard[5][0]="5"
	checkerboard[6][0]="6"
	checkerboard[7][0]="7"
	checkerboard[8][0]="8"

	# This doesnt work for some reason

	# checkerboard[1:8][0]="1","2","3","4","5","6","7","8"


	# this function lays out the checker pattern
	# checks for a pound sign above and next to it, forming a checker pattern
	for x in range (1,9):
		for y in range (1,9):
			if checkerboard[x][y-1]=="#":
				continue
			if checkerboard[x-1][y]=="#":
				continue
			checkerboard[x][y]="#"

	# Laying out the pieces

	for x in range(1,4):
		for y in range(1,9):
			if checkerboard[x][y]=="#":
				continue
			checkerboard[x][y]="b"

	for x in range (6,9):
		for y in range(1,9):
			if checkerboard[x][y]=="#":
				continue
			checkerboard[x][y]="w"

def printBoard():
	# prints out the checkerboard with pieces
	for x in range (0,9):
		print (" | ".join(checkerboard[x][0:9]))
		#print checkerboard[x][0:9] (additional way to print)

def main():

	initBoard()
	print('\nPlayer1 is white (w), and Player2 is black(b)\n')
	print('Type \'quit\' to quit.\n')
	while checkWin() == False:
		player = 1
		printBoard()
		playerMovement(player)
		if checkWin() == False:
			player = 2
			printBoard()
			playerMovement(player)

# check win condition

main()
