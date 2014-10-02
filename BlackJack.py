# Black Jack
# by Rafael Oquendo
10/1/2014
import sys
import random
"""I learned to program in C#, i love arrays hence why i am using lists here. I am sure 
there is a better way to program this but give me a break, this is my 
first week in python : ) """
def autoWin(userValue, dealerValue):
	if userValue == 21 and dealerValue == 21:
		print "User Value is %d and Dealer is %d Congrats User You Win" %(userValue, dealerValue)
		sys.exit()
	elif userValue == 21:
		print "User Value is %d and Dealer is %d. Congrats User You Win" %(userValue, dealerValue)
		sys.exit()


#changeTheAce is used inthe event that the users gets 2 a's in the beginning of the game
#its sets the value to 2 instead of 22
def changeTheAce(unknownVariable):
	if unknownVariable == 22:
		return 2
	else:
		return unknownVariable


#checkAce is used after the first value, in the event a user gets an Ace which higher than 21
#it will convert that ace to a 1
def checkAce(card, totalValue):
	newValue = card + totalValue
	if newValue > 21:
		return 1
	else:
		return card


#generateCardValue generates a random number from 0-12
def generateCardValue():
	return random.randint(0,12)


#generateCardsuite generates a random number from 0-3	
def generateCardSuite():
	return random.randint(0,3)
#realValue sends user the actual value of the card in play


def realValue(outputVal):
	value = outputVal + 2
	if value > 13:
		value = 11
	elif value > 10:
		value = 10
	return value
#totalValue takes a input to integer number and adds them up and sends it back to the user


def totalValue(x,y):
	return x + y
#autoWin checks to see if the user has 21 









def whoWon(user, dealer):
	print "#################################################################################"
	if user > dealer:
		print "User Score: ", user 
		print "Dealers Score: ",dealer
		print "CONGRATS YOU ARE THE WINNER"
	else:
		print "User Score: ", user 
		print "Dealers Score: ",dealer
		print "DEALER IS THE WINNER"

def checkWin(user,dealer):
	if user == 21:
		print "User Score: ", user 
		print "Dealers Score: ",dealer
		print "CONGRATS YOU ARE THE WINNER"

def isOver(user,dealer):
	if user > 21:
		print "User Score: ", user 
		print "Dealers Score: ",dealer
		print "You Lose"
		sys.exit()
"""
##########################################################################################
									Functions above
##########################################################################################

"""
cardType = [2,3,4,5,6,7,8,9,10,"j","q","k","a"]   # used to generate output for user
cardSuite = ["clubs", "diamonds", "hearts","spades"] #used to generate output for user
userHand = [] # this is going to save the users hand
dealerHand = [] # this is going to save the dealers hand
userTotalValue = 0
dealerTotalValue = 0

#Users Hand Generation
for x in range (0,2):
	userValue = generateCardValue() #calls the function generateCardValue
	userSuite = generateCardSuite() #generates card suit
	#based on values generated above we append the value into this new list
	userHand.append ([cardType[userValue],cardSuite[userSuite]])
	userRealValue = realValue(userValue) #gets realvalue from the card chosen
	userTotalValue = totalValue(userTotalValue,userRealValue)

#Dealers Hand Generation
for x in range (0,2):
	dealerValue = generateCardValue()
	dealerSuite = generateCardSuite()
	dealerHand.append ([cardType[dealerValue],cardSuite[dealerSuite]])
	dealerRealValue = realValue(dealerValue)
	dealerTotalValue = totalValue(dealerTotalValue, dealerRealValue)

#check to see if user won with 21 after initial start of game
autoWin(userTotalValue, dealerTotalValue)

#typically you are only allowed to see one of the dealers card hence the out put
print """Welcome to BlackJack..."""
print ""
print "Your Hand: ",userHand,"\n"
print "Dealers Hand", dealerHand

"""use this for later
#print "Dealers Hand: ",dealerHand[x], "[ XXXXXXXXXXX ]" 
"""

print userTotalValue, dealerTotalValue

checkWin(userTotalValue,dealerTotalValue)

play = True

while play:
	print "\nHit or Stay ?"
	print "Enter hit for Hit and stay for Stay"
	userOption = raw_input('> ')
	if userOption == 'hit' :
		userValue = generateCardValue()
		userRealValue = realValue(userValue)
		if userRealValue == 11:
			userRealValue = checkAce(userRealValue, userTotalValue)
		userSuite = generateCardSuite()
		userHand.append ([cardType[userValue],cardSuite[userSuite]])
		userTotalValue = totalValue(userTotalValue,userRealValue)
		print "Your Hand: ",userHand,"\n"
		print "Dealers Hand", dealerHand
		print userTotalValue, dealerTotalValue
		isOver(userTotalValue,dealerTotalValue)
	else :
		play = False
		print "Your total is ",userTotalValue

whoWon(userTotalValue, dealerTotalValue)

