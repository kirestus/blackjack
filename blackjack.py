import random
import os

#Create Decks of cards as lists
deck_of_cards = []
player_hand = []
dealer_hand = []

#small splashscreen before the game boots up
def intro():
	os.system("clear")
	print "\n"
	print "+----------------------------+"
	print "+  AIR BUD WORLD BLACK JACK  +"  
	print "+      -Puppy Holdem-        +"
	print "+----------------------------+"
	print "\n"

#check the value of the cards in your hand
def check_value(hand, whom):
	card_value = 0
	hand_value = 0
	for i in hand:
		i.split(" ")
		first_part = i[0]
		second_part = i[1]
		if second_part.isdigit() == True:
			card_value = 10;
		elif first_part.isdigit() == True:
			card_value = first_part
		elif first_part == 'Q' or first_part == 'J' or first_part == 'K':
			card_value = 10
		else:
			card_value = 1
		hand_value += int(card_value)
	if hand_value > 21:
		return "BUST"
	return hand_value

#Retruns the name of the suit of cards
def suit_name(suit):
	if suit == 0:
		sname = 'Clubs'
	elif suit == 1:
		sname = 'Spades'
	elif suit == 2:
		sname = 'Hearts'
	elif suit == 3:
		sname = "Diamonds"
		
	return sname;

#re numbers cards
def card_name(number):
	if number <= 10 and number > 1:
		return number
	elif number == 11:
		return ('J')
	elif number == 12:
		return ('Q')
	elif number == 13:
		return ('K')
	elif number == 1:
		return ('A')

#build the deck by creating a list of cards and asigning numbers to the suit
def makedeck():
	suit = 0
	for i in range(0,4):
		next_card = 0
		for i in range(0,13):
			next_card += 1
			deck_of_cards.append("%s of %s" % (card_name(next_card),suit_name(suit)))
		suit += 1
	
def shuffledeck():
	random.shuffle(deck_of_cards)

def displaydeck():
	for i in deck_of_cards:
		print i;

def drawcard(towhom, numberofcards):
	while(numberofcards > 0):
		nextcard = deck_of_cards.pop(0)
		numberofcards -= 1
		if towhom == 'player':
			player_hand.append(nextcard)
		else:
			dealer_hand.append(nextcard)

def gameround(i):
	endround = 0
	while endround == i:
		makedeck()
		shuffledeck()
		drawcard('player', 2)
		drawcard('dealer', 2)
		print "The Player has: %s" %player_hand
		print "The Dealer has A hidden card and: %s \n" %dealer_hand[1]
		hitorstay()
		ai()
		whowon()
		endround = 1;

def hitorstay():
	if (check_value(player_hand, 'player')) == "BUST":
		print "player Busts"
	else:
		choice = raw_input("Do you want to hit or stay?: ")
		if choice == 'hit'or choice == '1' or choice == 'Hit':
			drawcard('player',1)
			print "the player has %s" %player_hand
			print ("Hand Value:",check_value(player_hand, 'player'))
			print ("")
			hitorstay()
		else:
			print "You stay with %s" % player_hand
			print ("Hand Value:",check_value(player_hand, 'player'))
			
def gameloop():
	again = 'yes'
	playgame = 1
	while playgame == 1:
		if again == "yes" or again == "Yes" or again == "y":
			gameround(0)
			reset()
			again = raw_input("Care to play another hand?: ")
			os.system('clear')
		else:
			playgame = 0;
			
#tells the dealer to hit if he is sitting on less than a 16
def ai():
	while check_value(dealer_hand, 'dealer') < 16:
		drawcard('dealer',1)
	if check_value(dealer_hand, 'dealer') <= 21:
		print ("Dealer Stays")
	
def whowon():
	p_hand_value = check_value(player_hand, 'player')
	d_hand_value = check_value(dealer_hand, 'dealer')
	print "\nThe Player Has: %s" %player_hand
	print ('Player Hand Value: %s' % p_hand_value)
	print ("\nThe Dealer Has: %s" %dealer_hand)
	print ('Dealer Hand Value: %s\n'% d_hand_value)
	
	if p_hand_value > d_hand_value and p_hand_value <= 21 or d_hand_value == "BUST" and p_hand_value != "BUST":
		print "You Win!!"
	else:
		print "Dealer Wins"
		
def reset():
	del player_hand[:]
	del dealer_hand[:]
	del deck_of_cards[:]


intro()	
gameloop()
