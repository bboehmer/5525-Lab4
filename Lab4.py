dictOfSentences = {}
arrayInDictionary = []
dataSplit= []
dictionary = []
dictionaryID = []

with open('dictionary.txt') as fp:
    for line in fp:
        line = line[::-1]
        index=line.find('|')
        word=line[index+1:]
        num=line[:index]
        word=word[::-1]
        num=num[::-1]
        dictionary.append(word)
        dictionaryID.append(num)

with open('sentiment_labels.txt') as fp:
    next(fp)
    for line in fp:
        index = line.find('|')
        number= line[:index]
        numberInt = int(number)
        rating = line[index+1:]
        rating = rating.strip("\n")
        dictionaryID[numberInt]=rating

with open("datasetSplit.txt","r") as file:
    next(file)
    for line2 in file:
        index = line2.find(',')
        label = line2[index+1:]
        label = label.strip("\n")
        dataSplit.append(label)


with open("SOStr.txt","r") as fp:
    count=1
    total=1
    #countOfSentence =1;
    for line in fp:
        arrayInDictionary=[]
        splitOfSentence = dataSplit[count-1]
        arrayInDictionary.append(splitOfSentence)
        line = line.strip("\n")
        sentenceWithBar = line
        line = line.replace("|"," ")
        length = len(line)
        sentence = line
        #arrayInDictionary.append(countOfSentence)
        arrayInDictionary.append(sentence)
        #countOfSentence+=1
        if sentence in dictionary:
            total+=1
            indexOfSentence = dictionary.index(sentence)
            arrayInDictionary.append(indexOfSentence)
            sentimentOfSentence = dictionaryID[indexOfSentence]
            arrayInDictionary.append(sentimentOfSentence)

        arrayInDictionary.append(sentenceWithBar)
        dictOfSentences[count]=arrayInDictionary
        count+=1

count=1
countOfExtNeg=0
countOfNeg=0
countOfNeut=0
countOfPos=0
countOfExtPos=0
count2=0
while count<=len(dictOfSentences):
    array = dictOfSentences[count]
    if array[0] == '1':
        if float(array[3]) >= 0 and float(array[3]) <= 0.2:
            countOfExtNeg+=1
        if float(array[3]) > 0.2 and float(array[3]) <= 0.4:
            countOfNeg+=1
        if float(array[3]) > 0.4 and float(array[3]) <= 0.6:
            countOfNeut+=1
        if float(array[3]) > 0.6 and float(array[3]) <= 0.8:
            countOfPos+=1
        if float(array[3]) > 0.8 and float(array[3]) <= 1.0:
            countOfExtPos+=1
        count2+=1
    count+=1

probOfExtNeg=countOfExtNeg/count2
probOfNeg=countOfNeg/count2
probOfNeut=countOfNeut/count2
probOfPos=countOfPos/count2
probOfExtPos=countOfExtPos/count2

print("Number of entries in training set")
print(count2)
print()
print("Probability of Extremely Negative:")
print(probOfExtNeg)
print()
print("Probability of Negative:")
print(probOfNeg)
print()
print("Probability of Neutral:")
print(probOfNeut)
print()
print("Probability of Positive:")
print(probOfPos)
print()
print("Probability of Extremely Positive:")
print(probOfExtPos)
print()

dictOfWords = {}
# while count<=len(dictOfSentences):
#     array = dictOfSentences[count]
#     if array[0] == '1':
array = dictOfSentences[1]
sentence = array[4]
print(sentence)
word = sentence[:sentence.find('|')]
print(word)

#print("Number of sentences recognized in dictionary.txt")
#print(dictOfSentences[1])
