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
    words = re.findall(r'\w+', content, flags=re.IGNORECASE)
    if casesensitive == "Y":
        words = re.findall(r'\w+', content)

    countedwords = Counter(words)
    numbertokens = 0
    maxoccurencenumber = 0
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
                print("p(", key, "=", i/numbertokens)


def calculatebigram(content, casesensitive):
    contentsplit = content.split()
    dictwords = {}
    lswordCombined = []

    for i in range(len(contentsplit) - 1):
        word1 = contentsplit[i]
        word2 = contentsplit[i + 1]
        wordCombined = word1 + " " + word2
        wordFormatted = "p("+word2 + "|" + word1 + ")"
        if wordCombined not in lswordCombined:
            countword1 = re.findall(word1, content, flags=re.IGNORECASE)
            countwordcombined = re.findall(word2, content, flags=re.IGNORECASE)

            if casesensitive == "Y":
                countword1 = re.findall(word1, content)
                countwordcombined = re.findall(word2, content)

            probabilityOfCounterWord = len(countwordcombined)/len(countword1)
            dictwords[wordFormatted] = probabilityOfCounterWord
            lswordCombined.append(wordCombined)

    dictwords = sorted(dictwords.items(), key=operator.itemgetter(1))

    print("\nBigram:")
    print("In order of most occurrences")

    for i in range(len(dictwords)):
        print(dictwords[i][0], "=", dictwords[i][1])


filename = input("Please enter filename including extension\n")
casesensitive = input("Case sensitive? (Y/N)")
main(filename, casesensitive)