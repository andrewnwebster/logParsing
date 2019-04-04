import pandas as pd
import re
import os

class logEntries:
	def __init__(self):

		self.reportedParameters={
			'customerID':0,
			'blahSize':0,
		}

	def getcustomerID(self, tempLine):
		return re.search(r"CustomerId:(\d+)", tempLine).group(1)
	def getblahSize(self, tempLine):
		strBtyes=re.search(r"Blah Size:(\d+)", tempLine).group(1)
		return int(strBtyes)

class filesClass:
	def __init__(self):
		self.inputLogName='test_input_log.txt'
		self.outputLogName='test_output_log.txt'
		self.resultsLogName='test_results.txt'

		self.collectedLogEntriesDF=pd.DataFrame()
		self.collectedOutputFileDF=pd.DataFrame()

		self.firstLineMatch=0

	def exportOutputFile(self, filename, outputName):
		filename.to_csv(outputName, sep=',')	

	def findFirstLine(self,tempText):
		return re.compile(r"\d\d-\d\d-\d\d\d\d \d\d:\d\d:\d\d").search(tempText)
	def findSecondLine(self,tempText):
		return re.compile(r"Blah Size:").search(tempText)

