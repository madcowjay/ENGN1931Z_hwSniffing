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
# was about 7.5 between values. The larger byte was an overflow for when the angle went over 255.
# The values seemed to drift a little as they increased, so I back-calculated
# to find the 7.5 was closer to 7.4986

##################################################################
### YOUR CODE TO CREATE THE COMMAND SEQUENCE SHOULD GO BELOW HERE
##################################################################
import struct

# import anything else you might need here
email= "jason_webster@brown.edu" #REPLACE THIS
multiplier = 7.4986
home_stage = b'\x43\x04\x01\x00\x50\x01'
query_pos  = b'\x11\x04\x01\x00\x50\x01'
commandSequence = home_stage

front_pos  = b'\x53\x04\x06\x00\xd0\x01\x01\x00'
for angleToEncode in desiredAngles:
	screwTurnsToEncode =multiplier*angleToEncode
	wholeScrew = int(screwTurnsToEncode)
	fractionalScrew = screwTurnsToEncode - wholeScrew

	a = struct.pack('h',wholeScrew)
	b = struct.pack('>h',int(fractionalScrew*256))
	tail_pos = (b+a)[1:4] + struct.pack('h',0)[0:1]
	commandSequence = commandSequence + front_pos + tail_pos

commandSequence = commandSequence + query_pos
##################################################################
### DO NOT CHANGE THE FOLLOWING - Used in submission process
##################################################################
def yourSubmission():
	return {'email':email,'hw':'sniffing','input':serverRequest,'output':commandSequence}
