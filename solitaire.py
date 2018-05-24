#Solitaire

#Version 1.0

#variables：

deck = [('♠️', 1), ('♠️', 2), ('♠️', 3), ('♠️', 4), ('♠️', 5), ('♠️', 6), ('♠️', 7), ('♠️', 8), ('♠️', 9), ('♠️', 10), ('♠️', 11), ('♠️', 12), ('♠️', 13),
('♣️', 1), ('♣️', 2), ('♣️', 3), ('♣️', 4), ('♣️', 5), ('♣️', 6), ('♣️', 7), ('♣️', 8), ('♣️', 9), ('♣️', 10), ('♣️', 11), ('♣️', 12), ('♣️', 13),
('♥️', 1), ('♥️', 2), ('♥️', 3), ('♥️', 4), ('♥️', 5), ('♥️', 6), ('♥️', 7), ('♥️', 8), ('♥️', 9), ('♥️', 10), ('♥️', 11), ('♥️', 12), ('♥️', 13),
('♦️', 1), ('♦️', 2), ('♦️', 3), ('♦️', 4), ('♦️', 5), ('♦️', 6), ('♦️', 7), ('♦️', 8), ('♦️', 9), ('♦️', 10), ('♦️', 11), ('♦️', 12), ('♦️', 13)]

upDeck = [('♠️', 1), ('♠️', 2), ('♠️', 3), ('♠️', 4), ('♠️', 5), ('♠️', 6)]
upDeckReveal = len(upDeck) - 2

rowDict = {1: [[('♥️', 7)], 6], 2: [[], 5], 3: [[], 4], 4: [[], 3], 5: [[], 2], 6: [[], 1], 7: [[], 0]}

sendSpade = 0
sendClub = 0
sendHeart = 0
sendDiamond = 0

#functions:

def haveWon():
	'''
	Check if you have won, return true if you have, false otherwise
	'''
	return (sendSpade == 13 and sendClub == 13 and sendDiamond == 13 and sendHeart == 13)


def isDifferent(tupleA, tupleB):
	'''
	Check if tupleA[0] and tupleB[0] are different colors, return true if different, false if same
	'''
	if tupleA[0] == '♠️' or tupleA[0] == '♣️':
		return(tupleB[0] == '♥️' or tupleB[0] == '♦️')
	else:
		return(tupleB[0] == '♠️' or tupleB[0] == '♣️')

def isOneLarger(largeTuple, smallTuple):
	'''
	Check if largeTuple is larger than smallTuple by one
	'''
	return(largeTuple[-1] - smallTuple[-1] == 1)

def isConnectable(topTuple, bottomTuple):
	'''
	Check if the bottomTuple can be connected to the topTuple (different color and top one larger)
	'''
	return ((len(topTuple) == 0) or (isDifferent(topTuple, bottomTuple) and isOneLarger(topTuple, bottomTuple)))

def getCard(cardTuple):
	'''
	Turn the card tuple into a string
	'''
	return (cardTuple[0] + str(cardTuple[1]))


def getRow(rowIndex):
	'''
	Turn the list into graphics
	'''
	print(str(rowIndex) + '  ', end="")
	if len(rowDict[rowIndex][0]) == 0:
		print('O')
	else:
		while rowDict[rowIndex][1] >= len(rowDict[rowIndex][0]):
			rowDict[rowIndex][1] -= 1
		while rowDict[rowIndex][1] < 0:
			rowDict[rowIndex][1] += 1
		for i in range(rowDict[rowIndex][1]):
			print('[] ', end="")
		for card in rowDict[rowIndex][0][rowDict[rowIndex][1]:]:
			print(getCard(card) + ' ', end="")
	print()


def bring(rowIndex):
	'''
	Check condition, if true, take the element and append to the corresponding row, If false, print invalid move
	'''
	if upDeckReveal < len(upDeck):
		if len(rowDict[rowIndex][0]) == 0 or isConnectable(rowDict[rowIndex][0][-1], upDeck[upDeckReveal]):
			rowDict[rowIndex][0].append(upDeck.pop(upDeckReveal))
		else:
			print('Invalid move.')
	else:
		print('There is nothing on the upDeck.')


def move(moveFrom, moveLen, moveTo):
	'''
	Check condition, if true, take part of the list that is moveLen long from the end of the row moveFrom. Move the segment to the end of the row moveTo. After that, if no card revealed in the original row, reveal the last card of the row.
	If false, print invalid move
	'''

	if len(rowDict[moveTo][0]) == 0 or isConnectable(rowDict[moveTo][0][-1], rowDict[moveFrom][0][-moveLen]):
		rowDict[moveTo][0] += rowDict[moveFrom][0][-moveLen:]
		rowDict[moveFrom][0] = rowDict[moveFrom][0][:-moveLen]
		if len(rowDict[moveFrom][0]) <= rowDict[moveFrom][1]:
			rowDict[moveFrom][1] = len(rowDict[moveFrom][0]) - 1
	else:
		print('Invalid move.')

def send(rowIndex):
	'''
	Send the last card of the row up if applicable. If the input is 0, send the card from updeck Otherwise print invalid move
	'''
	if rowIndex == 0:
		if upDeck[upDeckReveal][0] == '♠️':
			global sendSpade
			if upDeck[upDeckReveal][1] - 1 == sendSpade:
				upDeck.pop(upDeckReveal)
				sendSpade += 1
			else:
				print('Invalid move')
		elif upDeck[upDeckReveal][0] == '♣️':
			global sendClub
			if upDeck[upDeckReveal][1] - 1 == sendClub:
				upDeck.pop(upDeckReveal)
				sendClub += 1
			else:
				print('Invalid move')
		elif upDeck[upDeckReveal][0] == '♥️':
			global sendHeart
			if upDeck[upDeckReveal][1] - 1 == sendHeart:
				upDeck.pop(upDeckReveal)
				sendHeart += 1
			else:
				print('Invalid move')
		elif upDeck[upDeckReveal][0] == '♦️':
			global sendDiamond
			if upDeck[upDeckReveal][1] - 1 == sendDiamond:
				upDeck.pop(upDeckReveal)
				sendDiamond += 1
			else:
				print('Invalid move')
	elif rowIndex <= 7:
		if rowDict[rowIndex][0][-1][0] == '♠️':
			if rowDict[rowIndex][0][-1][1] - 1 == sendSpade:
				rowDict[rowIndex][0].pop(len(rowDict[rowIndex][0]) - 1)
				sendSpade += 1
			else:
				print('Invalid move')
		elif rowDict[rowIndex][0][-1][0] == '♣️':
			if rowDict[rowIndex][0][-1][1] - 1 == sendClub:
				rowDict[rowIndex][0].pop(len(rowDict[rowIndex][0]) - 1)
				sendClub += 1
			else:
				print('Invalid move')
		elif rowDict[rowIndex][0][-1][0] == '♥️':
			if rowDict[rowIndex][0][-1][1] - 1 == sendHeart:
				rowDict[rowIndex][0].pop(len(rowDict[rowIndex][0]) - 1)
				sendHeart += 1
			else:
				print('Invalid move')
		elif rowDict[rowIndex][0][-1][0] == '♦️':
			if rowDict[rowIndex][0][-1][1] - 1 == sendDiamond:
				rowDict[rowIndex][0].pop(len(rowDict[rowIndex][0]) - 1)
				sendDiamond += 1
			else:
				print('Invalid move')
	else:
		print('Invalid move.')


#The program:
import random
random.shuffle(deck)
rowDict[1][0] = deck[0:7]
rowDict[2][0] = deck[7:13]
rowDict[3][0] = deck[13:18]
rowDict[4][0] = deck[18:22]
rowDict[5][0] = deck[22:25]
rowDict[6][0] = deck[25:27]
rowDict[7][0] = deck[27:28]
upDeck = deck[28:]
upDeckReveal = len(upDeck)

while not haveWon():
	print('♠️: ' + str(sendSpade) + '    ', end = '')
	print('♣️: ' + str(sendClub) + '    ', end = '')
	print('♥️: ' + str(sendHeart) + '    ', end = '')
	print('♦️: ' + str(sendDiamond))
	print()
	if upDeckReveal == 0:
		print('O  ', end = "")
	else:
		print('[]  ', end = "")
	if upDeckReveal == len(upDeck):
		print('')
	else:
		print(getCard(upDeck[upDeckReveal]))
	getRow(1)
	getRow(2)
	getRow(3)
	getRow(4)
	getRow(5)
	getRow(6)
	getRow(7)

	print('f: flip the top deck')
	print('b: bring the card down from the top deck')
	print('m: move cards between rows')
	print('s: send a card to the finishing slot')
	ans = input()
	if ans == 'f':
		if upDeckReveal == 0:
			upDeckReveal = len(upDeck)
		else:
			upDeckReveal -= 1
	elif ans == 'b':
		print('Which row do you want to bring the card to?')
		print('  1-7: corresponding row')
		try:
			row = int(input())
			if row >= 1 and row <= 7:
				bring(row)
			else:
				print('Please enter a number between 1-7.')
		except:
			print('Please enter a number between 1-7.')
	elif ans == 'm':
		print('Which row do you want to move from?')
		print('  1-7: corresponding row')
		try: 
			rowFrom = int(input())
			if rowFrom >= 1 and rowFrom <= 7:
				print('How many cards do you want to move?')
				try:
					num = int(input())
					if num >= 1 and num <= (len(rowDict[rowFrom][0]) - rowDict[rowFrom][1]):
						print('Which row do you want move the cards to?')
						print('  1-7: corresponding row')
						try:
							rowTo = int(input())
							if rowTo >= 1 and rowTo <= 7:
								move(rowFrom, num, rowTo)
							else:
								print('Please enter a number between 1-7.')
						except:
							print('Please enter a number between 1-7.')
					else:
						print('There are only ' + str(len(rowDict[rowFrom][0]) - rowDict[rowFrom][1]) + ' moveable cards.')
				except:
					print('There are only ' + str(len(rowDict[rowFrom][0]) - rowDict[rowFrom][1]) + ' moveable cards.')
			else:
				print('Please enter a number between 1-7.')
		except:
			print('Please enter a number between 1-7.')
	elif ans == 's':
		print('Which row do you want to send from?')
		print('  0: top deck')
		print('  1-7: corresponding row')
		try:
			rowIndex = int(input())
			if rowIndex >= 0 and rowIndex <= 7:
				send(rowIndex)
			else:
				print('Please enter a valid number.')
		except:
			print('Please enter a number between 0-7.')
	else:
		print('Please enter a valid letter.')
	print('---------------------------------------')
print('♠️: ' + str(sendSpade) + '    ', end = '')
print('♣️: ' + str(sendClub) + '    ', end = '')
print('♥️: ' + str(sendHeart) + '    ', end = '')
print('♦️: ' + str(sendDiamond) + '    ', end = '')
if upDeckReveal == 0:
	print('O  ', end = "")
else:
	print('[]  ', end = "")
if upDeckReveal == len(upDeck):
	print('')
else:
	print(getCard(upDeck[upDeckReveal]))
getRow(1)
getRow(2)
getRow(3)
getRow(4)
getRow(5)
getRow(6)
getRow(7)
print('Congratulations! You win!')
