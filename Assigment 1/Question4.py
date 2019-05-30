import re
from collections import Counter
import operator

def main(filename):
    f = open(filename, "r")
    if f.mode == 'r':
        contents = f.read()
        calculateunigram(contents)
    else:
        print("File not found")


def calculateunigram(content):
    words = re.findall(r'\w+', content, flags=re.IGNORECASE)
    countedwords = Counter(words)
    numbertokens = 0
    maxoccurencenumber = 0
    sorted_x = sorted(countedwords.items(), key=operator.itemgetter(1))
    for key,value in countedwords.items():
        numbertokens += value
        if value > maxoccurencenumber:
            maxoccurencenumber = value

    print("In order of most occurrences")
    for i in range(maxoccurencenumber, 0, -1):
        matchingwords = str(i)
        for key, value in countedwords.items():
            numbertokens += value
            if value == i:
                matchingwords += " " + key
        print(matchingwords, i/numbertokens)


filename = input("Please enter filename including extension\n")
main(filename)
