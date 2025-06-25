def removeElement(arr, target):
    if arr is None:
        return -1

    count = 0

    for index in range(len(arr)):

        if arr[index] != target:
            arr[count] = arr[index]

            count += 1

    return count


inputVal = [0, 1, 3, 0, 2, 2, 4, 2]
findVal = 2
response = removeElement(inputVal, findVal)
print(f'response {response}')
print(f'input value {inputVal}')


def moveNonZeroElementToEnd(arr):
    count = 0

    for index in range(len(arr)):

        if arr[index] != 0:
            arr[count] = arr[index]
            count += 1

    while count < len(arr):
        arr[count] = 0
        count += 1


zeroInput = [0, 1, 5, 0, 4, 6, 0, 0, 4]
moveNonZeroElementToEnd(zeroInput)
print(f'zero at end {zeroInput}')


def reverseStringWithSpaceIntact(inputStr: str) -> str:
    reverseStrVal = []
    if inputStr is not None:

        spaceIndex = []
        #         loop string to get space count index
        for index, value in enumerate(inputStr):
            if value == ' ':
                spaceIndex.append(index)

        maxLen = len(inputStr) - 1

        while (maxLen >= 0):
            reverseStrVal.append(inputStr[maxLen])
            maxLen -= 1

    reverseString =  ''.join(reverseStrVal).replace(" ", "")
    print(f'final reverse string {reverseString}')

    for val in spaceIndex:
        reverseString.


StringValue = "Welcome to Python Programming"
response = reverseStringWithSpaceIntact(StringValue)
print(f'reverse string: {response}')
