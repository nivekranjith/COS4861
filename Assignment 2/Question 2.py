import re

def main(filename):
    try:
        f = open(filename, "r")
        if f.mode == 'r':
            contents = f.read()
            findargmax(contents)
        else:
            print("File not found")

    except:
        filename = input("\nPlease enter training filename including extension\n")
        main(filename)

def appendspacetoword(w):
    return " " + w.group(0) + " "

def assignTagSet(filename):
    try:
        f = open(filename, "r")
        if f.mode == 'r':
            datatowrite = ""
            contents = f.read()

            if not casesensitive:
                contents = contents.lower()

            contents = re.sub(r"\b\w*[-']\w*\b(\b\w*[-']\w*\b)*|(\w+)", appendspacetoword , contents) #Add spaces between each non-word(exclude hyphenated and words with apostrophes)

            spacesplit = contents.split()
            for x in spacesplit:
                if not x.lower() in dictwordstagmap:
                    datatowrite += x + "/NN "
                    testresults.append(x + "/NN")
                else:
                    datatowrite += x + "/" + dictwordstagmap[x.lower()] + " "
                    testresults.append(x + "/" + dictwordstagmap[x.lower()])

            f = open(filename + "_tagged.txt", "w")
            f.write(datatowrite)
            f.close()
            print("===========================================Question 2(b)========================================")
            print("Tagging written to " + filename + "_tagged.txt")
            print("================================================================================================")

            filename = input("\nPlease enter golden filename including extension\n")
            constructconfusionmatrix(filename)
        else:
            print("File not found")

    except:
        filename = input("\nPlease enter second filename including extension\n")
        assignTagSet(filename)


def findargmax(contents):
    if not casesensitive:
        contents = contents.lower()

    spaceSplit = contents.split()
    dictWordsTagCount = {}
    totalCountPerWord = {}
    totalCountPerWordTag = {}

    for i in range(len(spaceSplit)):
        if not spaceSplit[i] in totalCountPerWordTag:
            totalCountPerWordTag[spaceSplit[i]] = 0
        totalCountPerWordTag[spaceSplit[i]] += 1

        slashsplit = spaceSplit[i].split("/")
        if not slashsplit[0] in totalCountPerWord:
            totalCountPerWord[slashsplit[0]] = 0
        totalCountPerWord[slashsplit[0]] += 1

    for wordtag in totalCountPerWordTag:
        wordtagTotalCount = totalCountPerWordTag[wordtag]
        wordtagsplit = wordtag.split("/")
        wordTotalCount = totalCountPerWord[wordtagsplit[0]]

        if not wordtagsplit[0] in dictWordsTagCount:
            dictWordsTagCount[wordtagsplit[0]] = {}
        if not wordtagsplit[1] in dictWordsTagCount[wordtagsplit[0]]:
            dictWordsTagCount[wordtagsplit[0]][wordtagsplit[1]] = 0
        dictWordsTagCount[wordtagsplit[0]][wordtagsplit[1]] = wordtagTotalCount/wordTotalCount

    print("===========================================Question 2(a)========================================")
    for x in dictWordsTagCount:
        maxCount = -1
        tagName = ""
        for tagcount in dictWordsTagCount[x]:
            if dictWordsTagCount[x][tagcount] > maxCount:
                maxCount = dictWordsTagCount[x][tagcount]
                tagName = tagcount

        print(x, "-", tagName)
        dictwordstagmap[x.lower()] = tagName
    print("================================================================================================")

    filename = input("\nPlease enter second filename including extension\n")
    assignTagSet(filename)

def constructconfusionmatrix(filename):
    try:
        f = open(filename, "r")
        if f.mode == 'r':
            contents = f.read()
            if not casesensitive:
                contents = contents.lower()

            alltags = []
            alltagscombination = {}

            spacesplit = contents.split()
            for x in spacesplit:
                wordtagsplit = x.split("/")
                alltags.append(wordtagsplit[1])

            for x in dictwordstagmap.values():
                ismatch = False
                for y in alltags:
                    if x.lower() == y.lower():
                        ismatch = True
                        break
                if not ismatch:
                    alltags.append(x)

            alltags = list(dict.fromkeys(alltags))

            for x in alltags:
                for y in alltags:
                    alltagscombination[x.lower()+"?"+y.lower()] = 0 # x is golden, y is trained

            for i in range(len(testresults)):
                goldentag = spacesplit[i].split("/")[1].strip()
                testresulttag = testresults[i].split("/")[1].strip()
                if goldentag.lower() + "?" + testresulttag.lower() in alltagscombination:
                    alltagscombination[goldentag.lower() + "?" + testresulttag.lower()] += 1

            goldentagheading = ""
            arrgoldentagheading = []
            matrixdata = ""
            for x in alltagscombination:
                if not x.split("?")[0] in arrgoldentagheading:
                    goldentagheading += "        " + x.split("?")[0]
                    arrgoldentagheading.append(x.split("?")[0])

            for x in arrgoldentagheading: #training
                matrixdata += x
                subtract = len(x)
                for y in arrgoldentagheading:  #golden
                    for z in range(8 + len(y) - subtract - len(str(alltagscombination[y + "?" + x]))):
                        matrixdata += " "
                    subtract = 0
                    matrixdata += str(alltagscombination[y + "?" + x])

                matrixdata += "\n"

            print("===========================================Question 2(c)========================================")
            print(goldentagheading)
            print(matrixdata)
            print("================================================================================================")


        else:
            print("File not found")

    except:
        filename = input("\nPlease enter golden filename including extension\n")
        constructconfusionmatrix(filename)

dictwordstagmap ={}
testresults = []
casesensitivetext = input("Case Sensitive? (Y/N) \n")
casesensitive = False
if casesensitivetext.lower() == "Y":
    casesensitive = True;

filename = input("Please enter training filename including extension\n")
main(filename)
