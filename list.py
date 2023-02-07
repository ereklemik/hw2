test_list = [1, 4, 5, 7, 8]
print("The list is : " + str(test_list))

counter = 0
for i in test_list:
    counter = counter + 1
print("Length of list is : " + str(counter))


def multiplyList(myList):
 
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result
 
test_list2 = [1, 2, 3]
print(multiplyList(test_list2))
