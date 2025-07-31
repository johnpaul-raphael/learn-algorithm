def squareNaturalNumber(inputVal: int):
    if inputVal:
        result = [i * i for i in range(1, inputVal + 1)]
        print(f'{result=}')


def extractEvenNumbers(inputVal: list):
    if inputVal:
        # evenNum = []
        # for i in inputVal:
        #     if i % 2 == 0:
        #         evenNum.append(i)
        evenNum = [i for i in inputVal if i % 2 == 0]
        print(f'{evenNum=}')


def flat2DList(inputVal: list):
    if inputVal:
        flatArray = []
        for i in inputVal:
            for j in i:
                flatArray.append(j)
        print(f'{flatArray=}')


def findNameWithStartIndex(inputVal: list, startIndex: str):
    if inputVal and startIndex:
        result = [i for i in inputVal if i.upper().startswith(startIndex.upper())]
        print(f'findNameWithStartIndex: {result}')


def convertStrToInt(inputVal: list):
    if inputVal:
        result = [int(i) for i in inputVal]
        print(f'convertStrToInt: {result=}')


def squareValueInDict(inputVal: int):
    if inputVal:
        # squareResult = {}
        # for i in range(1, inputVal + 1):
        #     squareResult[i] = i * i
        squareResult = {i: i * i for i in range(1, inputVal + 1)}
        print(f'{squareResult=}')


def filterValues(inputVal: dict, greaterVal: int):
    # if inputVal and greaterVal:
    #     filterResult = {}
    #     for key in inputVal.keys():
    #         if inputVal.get(key) > greaterVal:
    #             filterResult[key] = inputVal.get(key)
    #     print(f'{filterResult = }')

    if inputVal and greaterVal:
        filterResult = {key: value for key, value in inputVal.items() if value > greaterVal}

        print(f'{filterResult = }')


def countFrequencyItem(inputItem: list):
    if inputItem:
        frequency = {}
        {}
        for i in inputItem:
            if frequency.get(i) is None:
                frequency[i] = 1
            else:
                count = frequency.get(i)
                frequency[i] = count + 1

        print(f'{frequency=}')


def swapKeyValueFromDict( inputItem: dict):
    if inputItem:
        swapDict = {}
        for i in inputItem.keys():
            value = inputItem.get(i)
            swapDict[value] = i

        print(f'{swapDict=}')


swapKeyValueFromDict({'a': 1, 'b': 2, 'c': 3})
countFrequencyItem(['a', 'b', 'a', 'c', 'b', 'a'])
squareNaturalNumber(10)
extractEvenNumbers([3, 2, 5, 3, 6, 7, 1, 9])
flat2DList([[1, 2], [3, 4], [5, 6]])
findNameWithStartIndex(['Steve', 'Bob', 'Sandra', 'Alice'], 's')
convertStrToInt(['10', '20', '30'])
squareValueInDict(10)
filterValues({'John': 80, 'Tom': 45, 'Ana': 95}, 50)
