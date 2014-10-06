# Black Jack
# by Rafael Oquendo
10/1/2014
import sys
import random

"""I learned to program in C#, i love arrays hence why i am using lists here. I am sure 
there is a better way to program this but give me a break, this is my 
first week in python : ) """
#autoWin checks to see if the user has 21 
def autoWin(userValue, dealerValue):
	if userValue == 21 and dealerValue == 21:
		print "User Value is %d and Dealer is %d Congrats User You Win" %(userValue, dealerValue)
	elif userValue == 21:
		print "User Value is %d and Dealer is %d. Congrats User You Win" %(userValue, dealerValue)
		

#checkAce is used after the first value, in the event a user gets an Ace which higher than 21
#it will convert that ace to a 1
def checkAce(card, totalValue):
	newValue = card + totalValue
	if newValue > 21:
		return 1
	else:
		return card

#changeTheAce is used inthe event that the users gets 2 a's in the beginning of the game
#its sets the value to 2 instead of 22
def changeInitialAce(unknownVariable):
	if unknownVariable == 22:
		return 2
	else:
		return unknownVariable

def CheckWinner(user):
	if user == 21:
		return True


def DisplayHand(usersHand, dealersHand):
	print "Users Hand is:" ,usersHand
	print "Dealers Hand is:", dealersHand

		
def Greeting():
	print "|\t##################################################\t|"
	print "|\t\tHello and Welcome to BlackJack\t\t\t|"
	print "|\t\tHow To Play\t\t\t\t\t|"
	print "|\t\tThis program will generate 2 cards for you\t|"
	print "|\t\tYou can either choose to hit or stay\t\t|"
	print "|\t\tGood Luck\t\t\t\t\t|"
	print "|\t##################################################\t|\n"


def isOver(user,dealer):
	if user > 21:
		print "User Score: ", user 
		print "Dealers Score: ",dealer
		print "You Lose"
		return True

def realValue(faceCard):
	if faceCard == 'a':
		return 11
	if faceCard == 'j' or faceCard == 'q' or faceCard == 'k':
		return 10

	return faceCard


#totalValue takes a input to integer number and adds them up and sends it back to the user
def totalValue(card1,card2):
	if card1 + card2 == 22: # checks if user has 2 aces if so return the value of 2
		return 2

	return card1 + card2


def winnersAnnouncement(user, dealer):
	print "Congrats You are the Winner"
	print "Users Hand %d Dealers Hand %d " %(user, dealer)

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

"""
##########################################################################################
									Functions above
##########################################################################################

"""
cardType = [2,3,4,5,6,7,8,9,10,"j","q","k","a"]  # used to generate output for user
cardSuite = ["clubs", "diamonds", "hearts","spades"] #used to generate output for user
userHand = [] # this is going to save the users hand
dealerHand = [] # this is going to save the dealers hand
userTotalCardValue = 0
dealerTotalCardValue = 0

#Users Hand Generation
for x in range (0,2):
	userValue = random.choice(cardType) #Calls random to the cardType List
	userSuite = random.choice(cardSuite) #Calls random to cardSuite
	#based on values generated above we append the value into this new list
	userHand.append ([userValue,userSuite])	
	userCardValue = realValue(userValue)#gets the actual value from the card chosen
	userTotalCardValue = totalValue(userTotalCardValue,userCardValue) #adds up total value of cards


#Dealers Hand Generation Functionality are the same as above
for x in range (0,2):
	dealerValue = random.choice(cardType)
	dealerSuite = random.choice(cardSuite)
	dealerHand.append ([dealerValue,dealerSuite])
	dealerCardValue = realValue(dealerValue)
	dealerTotalCardValue = totalValue(dealerTotalCardValue, dealerCardValue)


Greeting() #calls greeting


DisplayHand(userHand, dealerHand) #used to display current hand


didUserWin = CheckWinner(userTotalCardValue) #checks to see if user won based off of first shuffle

if didUserWin == True:
	winnersAnnouncement(userTotalCardValue, dealerTotalCardValue)

userOption = " "
iLost = False

while userOption != 'stay' and didUserWin != True and iLost != True:
	print "\nHit or Stay ?"
	print "Enter hit for Hit and stay for Stay"
	userOption = raw_input('> ')
	if userOption == 'hit' :
		userValue = random.choice(cardType) #calls the function generateCardValue
		userSuite = random.choice(cardSuite) #generates card suit
		userHand.append ([userValue,userSuite])	#adds to list
		#if a is greater than 21 set it to 1
		if userValue == 'a': 
			userCardValue = checkAce(userCardValue, userTotalCardValue) #this function checks a's
			userTotalCardValue = userTotalCardValue + userCardValue
		else:
			userCardValue = realValue(userValue)#gets the actual value from the card chosen
			userTotalCardValue = totalValue(userTotalCardValue,userCardValue)
		DisplayHand(userHand, dealerHand)

		"""
		Ok here is what you need to work on next. Currently as it stands 
		If you go over 21 when you hit, it is not stoping this code
		Also take a look at the while loop do you really need userOption != 'stay'?
		or is that redundant?
		"""



		didUserWin = isOver(userTotalCardValue, dealerTotalCardValue)
		print userTotalCardValue, dealerTotalCardValue # i dont need this but good for testing
	


	
iLost = isOver(userTotalCardValue,dealerTotalCardValue)
whoWon(userTotalCardValue, dealerTotalCardValue)

"""
print userHand
print dealerHand
print userTotalCardValue
print dealerTotalCardValue
"""


