def CalculateMinEditDistance(str1,str2, insertWeight, deleteWeight, substituteWeight, showMatrix):

    str1length = len(str1) + 1
    str2length = len(str2) + 1
    matrix = [[0 for col in range(str1length)] for row in range(str2length)]

    for col in range(str1length):
        matrix[0][col] = col

    for row in range(str2length):
        matrix[row][0] = row

    for row in range(str2length):
        for col in range(str1length):
            if row > 0 and col > 0:
                if str1[col - 1] == str2[row - 1]:
                    matrix[row][col] = matrix[row - 1][col - 1]
                else:
                    matrix[row][col] = min(matrix[row - 1][col] + deleteWeight,
                                           matrix[row - 1][col - 1] + substituteWeight,
                                           matrix[row][col - 1] + insertWeight)

    if showMatrix == "Y":
        str1 = "#" + str1
        arrstr1 = [str1[i] for i in range(str1length)]

        str2 = "#" + str2
        arrstr2 = [[str2[i] for col in range(1)] for i in range(str2length)]

        print(arrstr2)
        for row in range(str2length):
            print(arrstr1[row], matrix[row])

    print("Answer is: ", matrix[str2length-1][str1length-1])


str1 = input("Please insert word 1")
str2 = input("Please insert word 2")
insertWeight = input("Please weighting for an insert")
deleteWeight = input("Please weighting for a delete")
substituteWeight = input("Please weighting for a substitute")
showMatrix = input("Return Matrix (Y/N)")

try:
    CalculateMinEditDistance(str1, str2, int(insertWeight), int(deleteWeight), int(substituteWeight),showMatrix)
except ValueError:
    print("Invalid input data")


