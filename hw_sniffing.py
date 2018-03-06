# Homework Sniffing Template Code
#
# This initial helper code will contact the server to request a list of desired angles, and will turn these comma separated values into a python list called desiredAngles.
#
# Your goal is to produce a command sequence that will:
#  - First home the stage
#  - Then move the stage to each position in the desiredAngle list
#  - Finally query the position of the stage at its final position.
#
# Pass your commands to the variable named commandSequence, and it will be save to a file unscrambledText.txt
#
# When you have a final answer, you can submit your assignment to the autograde by running the submit.py script

##################################################################
### HELPER CODE TO REQUEST DESIRED ANGLES FROM SERVER
##################################################################
import requests
serverRequest=requests.get("https://goo.gl/Y83I1i").text
desiredAngles=[float(x) for x in serverRequest.split(',')]
##################################################################
### YOUR BRIEF TEXT EXPLANATION OF YOUR DETECTIVE WORK
##################################################################

# Please provide a brief text explanation of how you decoded the stage commands

# The first command I decoded was home. By just pushing h, and then looking at the input.txt file,
# I saw that the byte structure is: 4304 0100 5001
# Then I just ran a q command and checked to find: 1101 0100 5001
# By entering just a single number at a time I saw the pattern for position requests is:
# 5304 0600 d001 0100 xxxx xxxx
# I ran a bunch of different values and recorded them into an Excel spreadsheet.
# Next, I comverted the bytes into decimal and separated them with commas.
# This actually made me think of my Ancient Astronomy class where the Babylonians Used
# a sexigesimal system which is modernly written with commas to separate the place values
# and a semicolon to represent the decimal point.
# These numbers looked similar and I noticed a difference of about 7 between entries in one
# of the columns. It became clear that the other column was fractional and I saw that the true difference
# was 7.5 bwtween values. The larger byte was an overflow for when the angle went over 255.

##################################################################
### YOUR CODE TO CREATE THE COMMAND SEQUENCE SHOULD GO BELOW HERE
##################################################################
import struct
import binascii
# import anything else you might need here
print(desiredAngles)
email= "jason_webster@brown.edu" #REPLACE THIS
temp = 7.4986
struct.pack('f', temp)
temp2 = 7
hex(7*2)
hex(int(.5*255*2))

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 20, 30, 40, 50, 100, 101, 200, 300, 400, 500, 360, 720]
for angleToEncode in values:
	#angleToEncode = values[i]
	screwTurnsToEncode =7.4986*angleToEncode
	wholeScrew = int(screwTurnsToEncode)
	fractionalScrew = screwTurnsToEncode - wholeScrew
	hex(wholeScrew)
	a3 = hex(int(fractionalScrew*256))
	#print(a3)
	b3 = '\\' + a3[1:]
	wholeScrewUpper = int(wholeScrew / 256)
	wholeScrewLower = (wholeScrew % 256)
	a2 = hex(wholeScrewUpper)
	#print(a2)
	b2 = '\\' + a2[1:]
	a1 = hex(wholeScrewLower)
	#print(a1)
	b1 = '\\' + a1[1:]
	#print(b2)
	if(len(b1)==3):
		b1 = b1[0:1] + '0' + b1[2]
	if(len(b2)==3):
		b2 = b2[0:2] + '0' + b2[2]
	if(len(b3)==3):
		b3 = b3[0:1] + '0' + b3[2]
	#print(a3 + a1 + a2)
	print(str(angleToEncode) + ':  ' + b3 + b1 + ' | ' + b2 + '\\x00')


commandSequence='???' # UPDATE THIS LINE TO INCLUDE YOU ANSWER

##################################################################
### DO NOT CHANGE THE FOLLOWING - Used in submission process
##################################################################
def yourSubmission():
	return {'email':email,'hw':'sniffing','input':serverRequest,'output':commandSequence}
