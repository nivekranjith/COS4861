import re
from collections import Counter
import operator


def main(filename, casesensitive):
    try:
        f = open(filename, "r")
        if f.mode == 'r':
            contents = f.read()
            calculateunigram(contents, casesensitive)
            calculatebigram(contents, casesensitive)
            main()
        else:
            print("File not found")

    except:
        filename = input("\nPlease enter filename including extension\n")
        casesensitive = input("Case sensitive? (Y/N)")
        main(filename, casesensitive)


def calculateunigram(content, casesensitive):
    words = re.findall(r'\w+', content)
    if casesensitive == "N":
        content = content.upper()
        words = re.findall(r'\w+', content)

    countedwords = Counter(words)
    numbertokens = 0
    maxoccurencenumber = 0
    nc = {}
    sorted_x = sorted(countedwords.items(), key=operator.itemgetter(1))
    for key, value in countedwords.items():
        numbertokens += value
        if value > maxoccurencenumber:
            maxoccurencenumber = value

    print("Unigram:")
    print("In order of most occurrences")
    for i in range(maxoccurencenumber, 0, -1):
        for key, value in countedwords.items():
            numbertokens += value
            if value == i:
                print("p(", key, ") =   ", i/numbertokens)
                if not nc.get(i):
                    nc[i] = 0
                nc[i] += 1

    goodturingdiscount(nc)


def calculatebigram(content, casesensitive):
    if casesensitive == "N":
        content = content.upper()

    contentsplit = content.split()
    dictwords = {}
    lswordCombined = []
    nc= {}

    for i in range(len(contentsplit) - 1):
        word1 = contentsplit[i]
        word2 = contentsplit[i + 1]
        wordCombined = word1 + " " + word2
        wordCombined2 = word1 + "\n" + word2
        wordFormatted = "p("+word2 + "|" + word1 + ")"
        if wordCombined not in lswordCombined:
            countword1 = re.findall(word1, content)
            countwordcombined = re.findall(wordCombined, content)
            countwordcombined2 = re.findall(wordCombined2, content)
            probabilityOfCounterWord = (len(countwordcombined)+ len(countwordcombined2))/len(countword1)
            dictwords[wordFormatted] = probabilityOfCounterWord
            lswordCombined.append(wordCombined)
            if not nc.get(len(countwordcombined) + len(countwordcombined2)):
                nc[len(countwordcombined)+ len(countwordcombined2)] = 0
            nc[len(countwordcombined)+ len(countwordcombined2)] += 1

    dictwords = sorted(dictwords.items(), key=operator.itemgetter(1))

    print("\nBigram:")
    print("In order of most occurrences")

    for i in range(len(dictwords)):
        print(dictwords[i][0], "=   ", dictwords[i][1])
    goodturingdiscount(nc)


def goodturingdiscount(nc):
    for key, value in nc.items():
        maxnc = key
        break

    global kthreshold
    lognc = {}
    listc = list(nc.keys())
    listc.sort()

    counter = 0

    for i in range(len(listc)):
        if i == 0 or i == len(listc) - 1:
            lognc[listc[i]] = nc[listc[i]]
        else:
            lognc[listc[i]] = nc[listc[i]] / (0.5 * (listc[i + 1] - listc[i - 1]))

    calculateRegressionLine(lognc)

    print("Good-Turing")

    for i in range(1,maxnc):
        if i <= kthreshold:
            if getNcValueFromRegressionline(i) == 0 or getNcValueFromRegressionline(kthreshold + 1):
                newcnumerator = 0
            else:
                newcnumerator = ((i + 1)*(getNcValueFromRegressionline(i+1)/getNcValueFromRegressionline(i))) / - i*((kthreshold + 1) * getNcValueFromRegressionline(kthreshold + 1))

            if getNcValueFromRegressionline(1) == 0:
                newc = 0
            else:
                newcdenominator = 1 - (((kthreshold + 1) * getNcValueFromRegressionline(kthreshold + 1))
                                       / getNcValueFromRegressionline(1))
                newc = newcnumerator / newcdenominator
            print("c:", i, "     c* =", newc)
        else:
            print("c:", i, "     c* =", i)

def calculateRegressionLine(data):
    avgy = 0
    avgx = 0
    avgxy = 0
    avgxsqrd = 0

    for key, value in data.items():
        avgx += key
        avgy += value
        avgxy == key*value
        avgxsqrd += key**2

    avgx = avgx / len(data)
    avgy = avgy / len(data)
    avgxy = avgxy / len(data)
    avgxsqrd = avgxsqrd / len(data)

    global gradient
    gradient = ((avgx * avgy) - avgxy) / (avgx ** 2 - avgxsqrd)
    global yint
    yint = avgy - gradient * avgx


def getNcValueFromRegressionline(x):
    global gradient
    global yint

    return gradient*x + yint


filename = input("Please enter filename including extension\n")
casesensitive = input("Case sensitive? (Y/N)")
kthreshold = input("Enter K Threshold")
if not kthreshold.isnumeric():
    kthreshold = 5
kthreshold = int(kthreshold)

main(filename, casesensitive)
