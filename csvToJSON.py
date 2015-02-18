#! /usr/env/python
# this script converts the csv energy tables into a JSON file

import io

#read in 2-2 loop
# FIRST ROW - comma is field separator
with open('/Users/sarahguermond/Files/Loop_2_2.csv', 'r') as infile:
	firstLine = infile.readline()

lineList = firstLine.strip().split(",")

loop_2_2 = {}
for string1 in lineList[1:]: #skip the first item because it's just table label
	if string1 not in loop_2_2:
		loop_2_2[string1] = {}
	else:
		continue


# ALL OTHER ROWS
#string2ToEnergy = io.open('/Users/sarahguermond/Files/Loop_2_2.csv', 'r')
#for line in string2ToEnergy:
#	lineList = line.strip().split(",")
#	string2 = lineList[0]
	# get index and value for all keys in loop_2_2 (col names)
#	for index, string1 in enumerate(loop_2_2):
#		loop_2_2[string1[string2]] = lineList[index+1]
#string2ToEnergy.close()


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