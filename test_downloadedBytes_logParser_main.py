import re
import os
import pandas as pd
import sys
import test_downloadedBytes_logParser_class as lpc

def main():
	filesClass_1=lpc.filesClass()

	with open(filesClass_1.inputLogName,'r') as f:
		for line in f:
			if line.strip():
				tempLine=(line.rstrip())
				firstLineMatch = filesClass_1.findFirstLine(tempLine)
				secondLineMatch = filesClass_1.findSecondLine(tempLine)

				if firstLineMatch is not None and filesClass_1.firstLineMatch==0:
					logEntriesClass_1=lpc.logEntries()
					logEntriesClass_1.reportedParameters['customerID']=logEntriesClass_1.getcustomerID(tempLine)
					filesClass_1.firstLineMatch=1
				elif secondLineMatch is not None and filesClass_1.firstLineMatch==1:
					logEntriesClass_1.reportedParameters['blahSize']=logEntriesClass_1.getblahSize(tempLine)
					#print(logEntriesClass_1.reportedParameters)
					filesClass_1.firstLineMatch=0
					filesClass_1.collectedLogEntriesDF=\
						pd.concat([filesClass_1.collectedLogEntriesDF, pd.DataFrame([logEntriesClass_1.reportedParameters])])
					del logEntriesClass_1
				else:
					filesClass_1.firstLineMatch=0
					del logEntriesClass_1
	
	filesClass_1.collectedOutputFileDF=\
		filesClass_1.collectedLogEntriesDF.groupby(['customerID']).sum()

	#print(filesClass_1.collectedLogEntriesDF)
	#print(filesClass_1.collectedOutputFileDF)
	#filesClass_1.exportOutputFile(filesClass_1.collectedLogEntriesDF, 'test_log.txt')

	filesClass_1.exportOutputFile(filesClass_1.collectedOutputFileDF, filesClass_1.resultsLogName)

main()
