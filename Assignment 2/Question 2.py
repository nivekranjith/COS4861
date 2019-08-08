def main(filename):
    try:
        f = open(filename, "r")
        if f.mode == 'r':
            contents = f.read()
            findargmax(contents)
            main()
        else:
            print("File not found")

    except:
        filename = input("\nPlease enter filename including extension\n")
        main(filename)


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


filename = input("Please enter filename including extension\n")
main(filename)
