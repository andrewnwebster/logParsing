import re
import pandas
'''
Notes:
Alternating Functions, based on line found -- push to next. If mismatch, start over

CLASS OBJECTS (LOG ENTRIES)

Set 1st line function found = 0
Set 1st line text = ''

Set 2nd line function found = 0
Set 2nd line text = ''

RegEx for CustomerID
RegEx for Blah Size

CLASS OBJECTS (INPUT FILE)
Set input file name = 'test_input_log.txt'
Set output file name = 'test_output_log.txt'

CLASS OBJECTS (OUTPUT FILE)
Set collected log entries DF = pd.DataFrame()
Set collected output file DF = pd.DataFrame()

Open File
with open(filename) as f:
    for line in f:
		if (find 1st line function /dated line AND 1st line function found = 0 AND 2nd line function found = 0)
			Create Class (LOG ENTRIES)
			Set 1st line text = '' WHATEVER IS IN THE LINE
			Set 1st line function found = 1
		else 
			capture out of sync line
			Set 1st line function found = 0
			Set 2nd line function found = 0
			(LOG ENTRIES)

		if (find 2nd line function /blah Size AND 1st line function found = 1 AND 2nd line function found = 0)
			Set 2nd line text = '' WHATEVER IS IN THE LINE
			Set 2nd line function found = 1
			[
				DO EVERYTHING
				COMBINE 1st and 2nd lines of text

				FIND CustomerId
				FIND Blah Size
				ADD found parameters to DF
			]
			Set 1st line function found = 0
			Set 2nd line function found = 0
			Delete Class (LOG ENTRIES)

		else
			capture out of sync line
			Set 1st line function found = 0
			Set 2nd line function found = 0
			Delete Class (LOG ENTRIES)



'''