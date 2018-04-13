sentencesWithNumber = []
with open("datasetSentences.txt","r") as fp:
    next(fp)
    for line in fp:
        sentencesWithNumber.append(line)
print("Number of sentences in datasetSentences.txt")
print(len(sentencesWithNumber))

dictionary = []
with open("dictionary.txt","r") as fp:
    for line in fp:
        size = len(line)
        dictionary.append(line[:-7])

plainSentences = []
for line in sentencesWithNumber:
    index=line.find("\t")
    test = line[index+1:]
    plainSentences.append(test)

arrayOfWords = []
arrayOfNumbers = []
with open('dictionary.txt') as fp:
    for line in fp:
        line = line[::-1]
        index=line.find('|')
        word=line[index+1:]
        num=line[:index]
        word=word[::-1]
        num=num[::-1]
        arrayOfWords.append(word)
        arrayOfNumbers.append(num)

with open('sentiment_labels.txt') as fp:
    next(fp)
    for line in fp:
        index = line.find('|')
        number= line[:index]
        numberInt = int(number)
        rating = line[index+1:]
        arrayOfNumbers[numberInt]=rating

#Now arrayofNum has the sentiment value of the dictionary word at its index aka arrayOfNum[1]= the sentiment value of the dictionary word with label 1

count=0
for line in plainSentences:
    length = len(line)
    line = line[:length-1]
    left = "'"
    if line in arrayOfWords:
        count=count+1

print("Number of sentences recognized in dictionary.txt")
print(count)
