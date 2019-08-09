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

def assignTagSet(filename):
    try:
        f = open(filename, "r")
        if f.mode == 'r':
            datatowrite = ""
            contents = f.read()

            if not casesensitive:
                contents = contents.lower()

            spacesplit = contents.split()
            for x in spacesplit:
                if not x.lower() in dictwordstagmap:
                    datatowrite += x + "/NN "
                else:
                    datatowrite += x + "/" + dictwordstagmap[x.lower()] + " "

            f = open(filename + "_tagged.txt", "w")
            f.write(datatowrite)
            f.close()
            print("Tagging written to " + filename + "_tagged.txt")
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
        dictWordsTagCount[wordtagsplit[0]][wordtagsplit[1]] = wordtagTotalCount/wordtagTotalCount

    for x in dictWordsTagCount:
        maxCount = -1
        tagName = ""
        for tagcount in dictWordsTagCount[x]:
            if dictWordsTagCount[x][tagcount] > maxCount:
                maxCount = dictWordsTagCount[x][tagcount]
                tagName = tagcount

        print(x, "-", tagName)
        dictwordstagmap[x.lower()] = tagName

    filename = input("\nPlease enter second filename including extension\n")
    assignTagSet(filename)

dictwordstagmap ={}
casesensitivetext = input("Case Sensitive? (Y/N) \n")
casesensitive = False
if casesensitivetext.lower() == "Y":
    casesensitive = True;

filename = input("Please enter training filename including extension\n")
main(filename)
