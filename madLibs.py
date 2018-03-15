# 1.reading a text file
# 2.replace crucial vocabularies
# 3.print contents of a new text file and creat a new text file

# 1.reading
fileName = str(input('File Name:'))
textFileR = open(fileName)
textStr = textFileR.read()
print(textStr)
textFileR.close()

# 2.replacing
textList = textStr.split(' ')
conditionList = ['ADJECTIVE', 'NOUN', 'VERB', 'ADVERB']
for i in range(len(textList)):
    if textList[i] in conditionList:
        textList[i] = input('Enter a/an %s:\n' % textList[i].lower())

# 3.printing and writing
textStr2 = ' '.join(textList)
print(textStr2)
fileNameList = fileName.split('.')
textFileW = open(fileNameList[0]+'(copy).'+fileNameList[-1], 'w')
textFileW.write(textStr2)
textFileW.close()
