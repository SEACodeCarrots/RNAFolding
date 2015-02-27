#! /usr/env/python
# this script converts the csv energy tables into a JSON file

import io
import pprint
import json

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


loop_2_2 = getValues('Loop_2_2.csv')
f = open('loop_2_2.json', 'w')
json.dump(loop_2_2, f)
f.close()

loop_1_2 = getValues('Loop_1_2.csv')
f = open('loop_1_2.json', 'w')
json.dump(loop_1_2, f)
f.close()

bulge_1nt = getValues('Bulge_1nt.csv')
f = open('bulge_1nt.json', 'w')
json.dump(bulge_1nt, f)
f.close()

bulge_2nt = getValues('Bulge_2nt.csv')
f = open('bulge_2nt.json', 'w')
json.dump(bulge_2nt, f)
f.close()

bulge_3nt = getValues('Bulge_3nt.csv')
f = open('bulge_3nt.json', 'w')
json.dump(bulge_3nt, f)
f.close()

bulge_4nt = getValues('Bulge_4nt.csv')
f = open('bulge_4nt.json', 'w')
json.dump(bulge_4nt, f)
f.close()

bulge_5nt = getValues('Bulge_5nt.csv')
f = open('bulge_5nt.json', 'w')
json.dump(bulge_5nt, f)
f.close()

bulge_6nt = getValues('Bulge_6nt.csv')
f = open('bulge_6nt.json', 'w')
json.dump(bulge_6nt, f)
f.close()

hairpin = getValues('Hairpin.csv')
f = open('hairpin.json', 'w')
json.dump(hairpin, f)
f.close()

loop_1_1_GG = getValues('Loop_1_1_GG.csv')
f = open('loop_1_1_GG.json', 'w')
json.dump(loop_1_1_GG, f)
f.close()

loop_1_1_UU = getValues('Loop_1_1_UU.csv')
f = open('loop_1_1_UU.json', 'w')
json.dump(loop_1_1_UU, f)
f.close()

loop_1_1_noboost = getValues('Loop_1_1.csv')
f = open('loop_1_1_noboost.json', 'w')
json.dump(loop_1_1_noboost, f)
f.close()

#rnaTypes = ['loop_2_2', 'loop_1_2', 'bulge_1nt', 'bulge_2nt', 'bulge_3nt',
#	'Bulge_4nt', 'Bulge_5nt', 'Bulge_6nt', 'Hairpin', 'Loop_1_1_GG', 'Loop_1_1_UU']

#for rna in rnaTypes:
#	f.open(rna + '.json', 'w')
#	json.dump(#what do i use here)
