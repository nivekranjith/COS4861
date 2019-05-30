def CalculateMinEditDistance(str1,str2, insertWeight, deleteWeight,substituteWeight):
    print(str1)
    print(str2)
    print(insertWeight)
    print(deleteWeight)
    print(substituteWeight)


str1 = input("Please insert word 1")
str2 = input("Please insert word 2")
insertWeight = input("Please weighting for an insert")
deleteWeight = input("Please weighting for a delete")
substituteWeight = input("Please weighting for a substitute")
CalculateMinEditDistance(str1, str2, insertWeight, deleteWeight, substituteWeight)

