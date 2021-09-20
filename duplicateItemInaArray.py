def itemPresent(duplicateItems, item):
    for element in duplicateItems:
        if element == item:
            return
    duplicateItems.append(item)


def duplicateitem(listofitems):
    duplicateitems = []
    for k in range(len(listofitems)):
        for i in range(len(listofitems)):
            if listofitems[k] == listofitems[i] and k != i:
                itemPresent(duplicateitems, listofitems[k])
    return duplicateitems


ListOfNumbers = []
while True:
    number = (input("Enter the number to add in the list and write E to print the input"))
    if(number == 'E' ):
        break
    ListOfNumbers.append(int(number))


print(duplicateitem(ListOfNumbers))
