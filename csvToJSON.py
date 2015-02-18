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
loop_1_2 = getValues('/Users/sarahguermond/Files/Loop_1_2.csv')
bulge_1nt = getValues('/Users/sarahguermond/Files/Bulge_1nt.csv')
bulge_2nt = getValues('/Users/sarahguermond/Files/Bulge_2nt.csv')
bulge_3nt = getValues('/Users/sarahguermond/Files/Bulge_3nt.csv')
bulge_4nt = getValues('/Users/sarahguermond/Files/Bulge_4nt.csv')
bulge_5nt = getValues('/Users/sarahguermond/Files/Bulge_5nt.csv')
bulge_6nt = getValues('/Users/sarahguermond/Files/Bulge_6nt.csv')
hairpin = getValues('/Users/sarahguermond/Files/Hairpin.csv')
loop_1_1_GG = getValues('/Users/sarahguermond/Files/Loop_1_1_GG.csv')
loop_1_1_UU = getValues('/Users/sarahguermond/Files/Loop_1_1_UU.csv')
loop_1_1_noboost = getValues('/Users/sarahguermond/Files/Loop_1_1.csv')

# TO DO:
# actually put this stuff into JSON and link to front end