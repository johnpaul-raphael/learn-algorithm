def reverseStr(mainStr):
    if mainStr:
        return mainStr[::-1]


def occurrenceChar(chars, occrChar):
    if chars != '':
        return chars.count(occrChar)


def subStringExist(mainStr: str, subStr: str):
    if mainStr != '' and subStr != '':
        return subStr in mainStr


def extractFirstAndLastChar(mainStr: str):
    if mainStr:
        print(mainStr[0], mainStr[-1])# print(mainStr[0], mainStr[-1], sep="*")


def splitString(mainStr, splitCount):
    if mainStr is not None:
        mainSplit = mainStr.split()
        return mainSplit[:splitCount]


def findVowels(mainStr: str):
    vowels = 'aeiou'
    vowelsOutput = []
    for char in mainStr:
        if char in vowels:
            vowelsOutput.append(char)

    return vowelsOutput


def removeSpace(mainStr: str):
    if mainStr is not None:
        return mainStr.replace(" ", "")


def countWords(mainStr: str):
    if mainStr is not None:
        return len(mainStr.split(' '))


def findPosition(mainStr: str, findStr: str):
    if mainStr is not None:
        return mainStr.find(findStr)


def replaceWord(mainStr: str, oldStr: str, newStr: str):
    if mainStr is not None and oldStr is not None and newStr is not None:
        return mainStr.replace(oldStr, newStr)


def evenNumber(n: int) -> list: # list comprehension
    return [number for number in range(1, n + 1) if number % 2 == 0]


output = reverseStr('Python')
print('reverseStr:', output)

output1 = occurrenceChar('banana', 'a')
print('occurrence char: ', output1)

output2 = subStringExist('data science is fun', 'data')
print(f'subStringExist: {output2}')

output3 = extractFirstAndLastChar('')
print(f'extractFirstAndLastChar: {output3}')

output4 = splitString('Python is an amazing language', 3)
print(f'splitString: {output4}')

output5 = findVowels('intelligence')
print(f'intelligence: {output5}')

output6 = removeSpace('Space removal test')
print(f'removeSpace {output6}')

output7 = countWords('Python is a high level language')
print(f'countWords: {output7}')

output8 = findPosition('The cat sat on the mat', 'cat')
print(f'findPosition {output8}')

output9 = replaceWord('That is a bad idea', 'bad', 'good')
print(f'replaceWord: {output9=}')
