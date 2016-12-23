#!/user/bin/python3

import csv
import sys
#import os
#import pickle



	
	
def bin_text_to_csv(inputFile):
	oldFile = open(inputFile, 'r')
	newFile = "{}{}".format(str(inputFile), "_csv")
	outFile = open(newFile, 'w')

	for line in oldFile:
		newLine = list(line)
		for char in newLine:
			outFile.write("{}{}".format(char, ","))
	 	if line[(len(line)-1)] == "," :
			line[(len(line)-1)] = " "
	oldFile.close()
	outFile.close()


#def __main__():
if len(sys.argv) > 1 :
	inputFile = sys.argv[1]
	bin_text_to_csv(inputFile)


