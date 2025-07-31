i = 'python'
k = 3
result = ''

s = 0
loopCount = len(i) // k
while loopCount > 0:
    l = s + k
    while s < l:
        result += i[l - 1]
        l -= 1
    s += k
    loopCount -= 1
print(f'{result=}')