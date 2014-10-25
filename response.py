# program to calculate response from number chosen 0-10


# defining variables
s = 0
response = ['You are so modest.  I love you', 'I love your arms, they are very sexy', 'You have the most gorgeous smile!','You make me so happy', 'I love your geeky cuteness',
'I love your calmness and the way it hides your secret humour until the moment of perfect timing', 'I love that you know the stars',
'I want to cuddle you...forever', 'Mmmmmmmmm.... you!  I love you!', 'That expression!  You know the one.  The one that makes me want to...', 
'I love you <3' ]
# len = count(list)
tot = (len(response)) - 1

while True:

# ask user for number, check it is numeric
	choice = raw_input('Enter a number between 0 and %d' % tot)  


	# check value entered is a number between 0 and total number of responses-1
	# if it isn't propt for reentry
	# if it is, print the appropriate response line
	while True:
		try:
			s = int(choice)
			if s > tot or s < 0 :
				choice = raw_input('Which bit of between 0 and %d was hard to understand?  Try again, my love.' % tot) 
			else:
				break
		except:
			print "that isn't a whole number.  Try again"
			choice = raw_input('Enter an integer between 0 and %d, inclusive' % tot)
	print response[s]

	# see if they want another go
	answer = raw_input('do you want to try again? Y/N')
	# convert answer to lowercase
	answer = answer.lower()
	if answer == 'no' or answer == 'n':
		break
	


