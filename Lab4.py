dictOfSentences = {}
arrayInDictionary = []
dataSplit= []
dictionary = []
dictionaryID = []

#Get values from dictionary file and put the words in array called dictionary and corresponding ID in dictionaryID array
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

#Get values from sentiment_labels file and update dictionaryID with appropriate sentiment value
with open('sentiment_labels.txt') as fp:
    next(fp)
    for line in fp:
        index = line.find('|')
        number= line[:index]
        numberInt = int(number)
        rating = line[index+1:]
        rating = rating.strip("\n")
        dictionaryID[numberInt]=rating

#Get values from datasetSplit file and put them in array dataSplit
with open("datasetSplit.txt","r") as file:
    next(file)
    for line2 in file:
        index = line2.find(',')
        label = line2[index+1:]
        label = label.strip("\n")
        dataSplit.append(label)

#Get sentences from SOStr file and create the dictionary for the sentences that has [splitLabel, Sentence, index in dictionary array, sentiment Score, and Sentence with | between words]
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

#Count the number of times that a sentence in the training data and dev data is labeled with a specific sentiment (ext neg, neg, neut, pos, ext pos)
count=1
countOfExtNeg=0
countOfNeg=0
countOfNeut=0
countOfPos=0
countOfExtPos=0
numOfSentences=0
while count<=len(dictOfSentences):
    array = dictOfSentences[count]
    if array[0] == '1' or array[0] == '3':
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
        numOfSentences+=1
    count+=1

#Create probabilities of the sentence being each of the sentiment labels by dividing counts by total number of sentences.
probOfExtNeg=countOfExtNeg/numOfSentences
probOfNeg=countOfNeg/numOfSentences
probOfNeut=countOfNeut/numOfSentences
probOfPos=countOfPos/numOfSentences
probOfExtPos=countOfExtPos/numOfSentences

print("Number of entries in training set:",numOfSentences)
print()
print("Probability of Extremely Negative Sentences:",probOfExtNeg)
print("Probability of Negative Sentences:",probOfNeg)
print("Probability of Neutral Sentences:",probOfNeut)
print("Probability of Positive Sentences:",probOfPos)
print("Probability of Extremely Positive Sentences:",probOfExtPos)
print()

#Loop through each sentence in the training or dev set and add all the words to a dictionary for the words
dictOfWords = {}
count=1
while count<=len(dictOfSentences):
    array = dictOfSentences[count]
    flag=0
    sentence = array[4]
    if array[0] == '1' or array[0] == '3':
        while flag == 0:
            #If not on the last word in the sentence
            if sentence.find('|') != -1:
                #Get the word before the |
                word = sentence[:sentence.find('|')]
                #If it is not in the dictionary then create a new entry with a empty array [0,0,0,0,0,0] in it
                #This array will represent how many times the word has appeared in a sentence with a specific sentiment
                #This array will be something like [a,b,c,d,e,f] where a-e represent the count of times that word is in sentence with sentiment
                #ex: if a = 100 then the word appears in neg sentences 100 times etc
                #The value in f is the total number of times the word appears
                if word not in dictOfWords:
                    arrayOfTimes=[0,0,0,0,0,0]
                    if float(array[3]) >= 0 and float(array[3]) <= 0.2:
                        arrayOfTimes[0]=1
                    if float(array[3]) > 0.2 and float(array[3]) <= 0.4:
                        arrayOfTimes[1]=1
                    if float(array[3]) > 0.4 and float(array[3]) <= 0.6:
                        arrayOfTimes[2]=1
                    if float(array[3]) > 0.6 and float(array[3]) <= 0.8:
                        arrayOfTimes[3]=1
                    if float(array[3]) > 0.8 and float(array[3]) <= 1.0:
                        arrayOfTimes[4]=1
                    numOfOccurence=arrayOfTimes[5]
                    numOfOccurence+=1
                    arrayOfTimes[5] = numOfOccurence
                    dictOfWords[word]=arrayOfTimes
                else:
                    arrayOfTimes = dictOfWords[word]
                    if float(array[3]) >= 0 and float(array[3]) <= 0.2:
                        number = arrayOfTimes[0]
                        number+=1
                        arrayOfTimes[0]=number
                    if float(array[3]) > 0.2 and float(array[3]) <= 0.4:
                        number = arrayOfTimes[1]
                        number+=1
                        arrayOfTimes[1]=number
                    if float(array[3]) > 0.4 and float(array[3]) <= 0.6:
                        number = arrayOfTimes[2]
                        number+=1
                        arrayOfTimes[2]=number
                    if float(array[3]) > 0.6 and float(array[3]) <= 0.8:
                        number = arrayOfTimes[3]
                        number+=1
                        arrayOfTimes[3]=number
                    if float(array[3]) > 0.8 and float(array[3]) <= 1.0:
                        number = arrayOfTimes[4]
                        number+=1
                        arrayOfTimes[4]=number
                    numOfOccurence=arrayOfTimes[5]
                    numOfOccurence+=1
                    arrayOfTimes[5] = numOfOccurence

                sentence = sentence[sentence.find('|')+1:]

            #If we are on the last word of the sentence then just do the same thing as above but just on one word
            else:
                word = sentence
                if word in dictOfWords:
                    arrayOfTimes = dictOfWords[word]
                    if float(array[3]) >= 0 and float(array[3]) <= 0.2:
                        number = arrayOfTimes[0]
                        number+=1
                        arrayOfTimes[0]=number
                    if float(array[3]) > 0.2 and float(array[3]) <= 0.4:
                        number = arrayOfTimes[1]
                        number+=1
                        arrayOfTimes[1]=number
                    if float(array[3]) > 0.4 and float(array[3]) <= 0.6:
                        number = arrayOfTimes[2]
                        number+=1
                        arrayOfTimes[2]=number
                    if float(array[3]) > 0.6 and float(array[3]) <= 0.8:
                        number = arrayOfTimes[3]
                        number+=1
                        arrayOfTimes[3]=number
                    if float(array[3]) > 0.8 and float(array[3]) <= 1.0:
                        number = arrayOfTimes[4]
                        number+=1
                        arrayOfTimes[4]=number
                    numOfOccurence=arrayOfTimes[5]
                    numOfOccurence+=1
                    arrayOfTimes[5] = numOfOccurence
                else:
                    arrayOfTimes=[0,0,0,0,0,0]
                    if float(array[3]) >= 0 and float(array[3]) <= 0.2:
                        arrayOfTimes[0]=1
                    if float(array[3]) > 0.2 and float(array[3]) <= 0.4:
                        arrayOfTimes[1]=1
                    if float(array[3]) > 0.4 and float(array[3]) <= 0.6:
                        arrayOfTimes[2]=1
                    if float(array[3]) > 0.6 and float(array[3]) <= 0.8:
                        arrayOfTimes[3]=1
                    if float(array[3]) > 0.8 and float(array[3]) <= 1.0:
                        arrayOfTimes[4]=1

                    numOfOccurence=arrayOfTimes[5]
                    numOfOccurence+=1
                    arrayOfTimes[5] = numOfOccurence
                    dictOfWords[word]=arrayOfTimes
                flag=1
    count+=1

#Now create a dictionary for the probability of a sentiment given a certain word
dictOfProb={}
#For each word in the dictionary create an entry in dictionary of Probability
#Associated with each word is an array [a,b,c,d,e] where a is the probability
#that
for word in dictOfWords:
    array = dictOfWords[word]
    array2=[0,0,0,0,0]
    sum = array[0]+array[1]+array[2]+array[3]+array[4]
    array2[0]=array[0]/sum
    array2[1]=array[1]/sum
    array2[2]=array[2]/sum
    array2[3]=array[3]/sum
    array2[4]=array[4]/sum
    dictOfProb[word]=array2

print("Number of times the word \"the\" shows up in the training data")
print(dictOfWords["the"])
print("Probability the word \"the\" shows up in a sentence with label [ext neg, neg, neut, pos, ext pos]")
print(dictOfProb["the"])

#Sum the number of times each word was seen to get total number of words used
total=0
for word in dictOfWords:
    array = dictOfWords[word]
    total+=array[5]

count=1
count1=0
count2=0
count3=0
count4=0
count5=0

correct=0
incorrect=0
#For each sentence from the dictionary of sentences
while count<=len(dictOfSentences):
    sentenceIsExtNeg=0
    sentenceIsNeg=0
    sentenceIsNeut=0
    sentenceIsPos=0
    sentenceIsExtPos=0
    #Get the array associated with the sentence
    array = dictOfSentences[count]
    flag=0
    sentence = array[4]
    #If the sentence is part of the test set then lets test it
    if array[0] == '2':
        while flag == 0:
            #If we are not on the last word of the sentence
            if sentence.find('|') != -1:
                word = sentence[:sentence.find('|')]
                #If the current word has been seen before then calculate the naive bayes for that word for all 5 possible sentiments and add it to the running total
                if word in dictOfWords:
                    array2 = dictOfProb[word]
                    array3= dictOfWords[word]
                    #This calculation is the P(word being in a ext neg sentence)*P(extremely negative sentence)/(P(word)= # times that word appears/total number of any word appearing))
                    sentenceIsExtNeg+=((array2[0]*probOfExtNeg)/(array3[5]/total))
                    sentenceIsNeg+=((array2[1]*probOfNeg)/(array3[5]/total))
                    sentenceIsNeut+=((array2[2]*probOfNeut)/(array3[5]/total))
                    sentenceIsPos+=((array2[3]*probOfPos)/(array3[5]/total))
                    sentenceIsExtPos+=((array2[4]*probOfExtPos)/(array3[5]/total))
                #If the current word has not been seen before then calculate the naive bayes for that word using equal proability for every sentiment
                else:
                    sentenceIsExtNeg+=((0.2*probOfExtNeg)/(1/total))
                    sentenceIsNeg+=((0.2*probOfNeg)/(1/total))
                    sentenceIsNeut+=((0.2*probOfNeut)/(1/total))
                    sentenceIsPos+=((0.2*probOfPos)/(1/total))
                    sentenceIsExtPos+=((0.2*probOfExtPos)/(1/total))
                #Cut off the current word from sentence
                sentence = sentence[sentence.find('|')+1:]
            #If we are on the last word of the sentence do the same thing as above
            else:
                word = sentence
                if word in dictOfWords:
                    array2 = dictOfProb[word]
                    array3= dictOfWords[word]
                    sentenceIsExtNeg+=((array2[0]*probOfExtNeg)/(array3[5]/total))
                    sentenceIsNeg+=((array2[1]*probOfNeg)/(array3[5]/total))
                    sentenceIsNeut+=((array2[2]*probOfNeut)/(array3[5]/total))
                    sentenceIsPos+=((array2[3]*probOfPos)/(array3[5]/total))
                    sentenceIsExtPos+=((array2[4]*probOfExtPos)/(array3[5]/total))
                else:
                    sentenceIsExtNeg+=((0.2*probOfExtNeg)/(1/total))
                    sentenceIsNeg+=((0.2*probOfNeg)/(1/total))
                    sentenceIsNeut+=((0.2*probOfNeut)/(1/total))
                    sentenceIsPos+=((0.2*probOfPos)/(1/total))
                    sentenceIsExtPos+=((0.2*probOfExtPos)/(1/total))
                flag=1

        #Now that we have a score for each sentiment given the current sentence then we just choose the one with the highest score
        scores=[sentenceIsExtNeg,sentenceIsNeg,sentenceIsNeut,sentenceIsPos,sentenceIsExtPos]
        if max(scores)==sentenceIsExtNeg:
            #This is a count for how many were assigned to ext neg
            count1+=1
            #Check if the sentiment we chose matches the one provided in thedictionary. If yes then add to correct if no then add to incorrect
            if float(array[3]) >= 0 and float(array[3]) <= 0.2:
                correct+=1
            else:
                incorrect+=1
        if max(scores)==sentenceIsNeg:
            count2+=1
            if float(array[3]) >= 0.2 and float(array[3]) <= 0.4:
                correct+=1
            else:
                incorrect+=1
        if max(scores)==sentenceIsNeut:
            count3+=1
            if float(array[3]) >= 0.4 and float(array[3]) <= 0.6:
                correct+=1
            else:
                incorrect+=1
        if max(scores)==sentenceIsPos:
            count4+=1
            if float(array[3]) >= 0.6 and float(array[3]) <= 0.8:
                correct+=1
            else:
                incorrect+=1
        if max(scores)==sentenceIsExtPos:
            count5+=1
            if float(array[3]) >= 0.8 and float(array[3]) <= 1.0:
                correct+=1
            else:
                incorrect+=1
    count+=1

print()
print("Results from testing classifier on Test sentences:")
print(count1,"\t sentences assigned to extremely negative")
print(count2,"\t sentences assigned to negative")
print(count3,"\t sentences assigned to neutral")
print(count4,"\t sentences assigned to positive")
print(count5,"\t sentences assigned to extremely positive")
print()
print("Correct Predictions:",correct)
print("Incorrect Predictions:",incorrect)
print("Accuracy of Classifier on Test Data:",(correct/(correct+incorrect))*100)
