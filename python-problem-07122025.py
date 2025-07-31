def sqrt(i: int) -> int:
    if not i:
        print('empty input')
        return i

    loop = i // 2
    begin = 0
    end = loop - 1
    count = 1
    while begin <= end:
        middle = (begin + end) // 2
        # print(f'loop count {count} and {middle}')
        sqrtVal = middle * middle
        if sqrtVal == i:
            print(f'found the root value {middle}')
            return middle
        elif sqrtVal < i:
            begin = middle + 1
        else:
            end = middle - 1
        count += 1
    return -1


# for i in range(1, 101):
#     print(f'{i = } {sqrt(i) = }')


# print(f'{sqrt(0)=}')

# #########################################################################################
# pseudo code
# 1. Ugly Number
# 2. Super Ugly Number (Advanced)
#
# 3. Digital Sum / Digital Root
# write a recursive function check if digits greater than 1 then sum then ex input = 256 then 2+5+6 = 17 again call recursive with 17 =

# 4. Happy Number
# write recursive function that accept argument and loop the digits and do a multiply by itself and sumup and
# return the value if its equal to 1 then its happy number else unhappy
# question how to terminate infinite loop? --> have set and check if same sum is repeated then terminate

#
# 5. Sum of Digits of n! 5 1,2,3,4,5
# range given numbers into list ex. i = 3 inputVal = [1,2,3]
# loop list and result = result * i
# another loop for val in result then finalResult += result

def digitalRoot(inputVal: int) -> int:
    def sumDigits(n: int):
        total = 0
        while n > 0:
            digit = n % 10
            print(f'{digit=}')
            total += digit
            n = n // 10
        return total

    if inputVal < 10:
        return inputVal

    return digitalRoot(sumDigits(inputVal))


resultDigit = digitalRoot(12345)
print(f'{resultDigit=}')
