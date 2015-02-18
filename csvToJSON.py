#! /usr/env/python
# this script converts the csv energy tables into a JSON file

import io
import pprint

def getValues(fileName):
	#read in 2-2 loop
	infile = io.open(fileName, 'r')
	# get only first line
	firstLine = infile.readline()
	lineList = firstLine.strip().split(",")
	colsToRowsToValues = {}
	for col in lineList[1:]: #skip the first item because it's just table label
		if col not in colsToRowsToValues:
			colsToRowsToValues[col] = {}
		else:
			continue
	# get all the other rows		
	for line in infile:
		lineList = line.strip().split(",")
		row = lineList[0] # row names
		# get index and value for all keys in loop_2_2 (col names)
		num = 1
		for col, value in colsToRowsToValues.iteritems():
			if row not in colsToRowsToValues[col]:
				colsToRowsToValues[col][row] = lineList[num]
			num += 1
	infile.close()
	return colsToRowsToValues


loop_2_2_test = getValues('/Users/sarahguermond/Files/Loop_2_2.csv')
#pprint.pprint(loop_2_2)

loop_1_2 = getValues('/Users/sarahguermond/Files/Loop_1_2.csv')
pprint.pprint(loop_1_2)

# all other rows
# for string1 in dictionary1:
	# string1[first field] = value

#read in hairpins
#hairpins = io.open('~/Files/EnergyChart_Hairpin.csv', 'r')

#read in 1-2 loop
#loop_1_2 = io.open('~/Files/EnergyChart_1_2Loop.csv', 'r')

#read in 1-1 loop
#loop_1_1 = io.open('~/Files/EnergyChart_1_1Loop.csv', 'r')

#read in bulge
#bulge = io.open('~/Files/EnergyChart_Bulge.csv', 'r')

#make typeToSubtype
#make subtypeTo1stNuc
