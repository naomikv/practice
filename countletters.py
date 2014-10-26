# opens a text file and counts how many of each letter are in it
# variables
i = 0
j = 0

# f is name of the text file object
f = open('A Strip of Woods at the Back of the Mind.txt')


# check got it ok by printing contents
textfromfile = f.read()
# print textfromfile

# create empty dictionary.  A dictionary is a series of pairs of values (e.g. word and definition)
dict = {}

# work out which characters exist in the string, save to variable char
while i < len(textfromfile):
	char = textfromfile[i]
	
	# remove all non-letter characters
	if char.isalpha():
	
		# make all lower case
		char = char.lower()
	
		#check if character is in dictionary yet, if so add 1 to count, if not, start count at one
		if dict.has_key(char):
			dict[char] = dict[char] + 1
		else:
			dict[char] = 1	
	i = i + 1

# sort the letters in the poem alphabetically
azchar = sorted(dict)

# link az char list with count in dict and print character - count
for ealett in azchar:

# prints letter and count
#	print ealett + ' - ' + str(dict[ealett]) 

# make a functional but not terribly pretty graph of output values
# prints number of * corresponding to count of char ealett
# to avoid confusion with all the stars
#	bar = '*' * dict[ealett]

#	print ealett + '|' + bar

# prints each line of graph filled with appropriate letter
	print ealett * dict[ealett]

''' 
output:
	aaaaaa
	bbbbbbbbbbbb
	ccc
	etc.
'''
