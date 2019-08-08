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
    spaceSplit = contents.split()
    dictWordsTagCount = {}
    for i in range(len(spaceSplit)):
        slashsplit = spaceSplit[i].split("/")
        if not slashsplit[0] in dictWordsTagCount:
            dictWordsTagCount[slashsplit[0]] ={}
        if not slashsplit[1] in dictWordsTagCount[slashsplit[0]]:
            dictWordsTagCount[slashsplit[0]][slashsplit[1]] = 0
        dictWordsTagCount[slashsplit[0]][slashsplit[1]] += 1

    for x in dictWordsTagCount:
        maxCount = -1
        tagName = ""
        for tagcount in dictWordsTagCount[x]:
            if dictWordsTagCount[x][tagcount] > maxCount:
                maxCount = dictWordsTagCount[x][tagcount]
                tagName = tagcount

        print(x,"-",tagName)
        dictwordstagmap[x.lower()] = tagName

    filename = input("\nPlease enter second filename including extension\n")
    assignTagSet(filename)

dictwordstagmap ={}
filename = input("Please enter training filename including extension\n")
main(filename)
