# 1.reading a text file
# 2.replace crucial vocabularies
# 3.print contents of a new text file and creat a new text file

import re

# 1.reading
fileName = str(input('File Name:'))
textFileR = open(fileName)
textStr = textFileR.read()
print(textStr)
textFileR.close()

# 2.replacing
conditionList = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')
conditionText = conditionList.findall(textStr)
for words in conditionText:
    newWords = str(input('Enter a/an %s:\n' % words))
    textStr = textStr.replace(words, newWords, 1)
# 3.printing and writing
print(textStr)
fileNameList = fileName.split('.')
textFileW = open(fileNameList[0]+'(copy).'+fileNameList[-1], 'w')
textFileW.write(textStr)
textFileW.close()
