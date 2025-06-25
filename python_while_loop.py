class Solution:
    def calculate(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        index = 0
        print(f'nums: {nums}')
        while index <= len(nums) - 1:
            print(f'index: {index} and value: {nums[index]}')
            index += 1  # Increment index to avoid infinite loop


# sol = Solution()
# sol.calculate()


def closestNumber(self, n , m):
        # code here 
        divisible = n % m
        
        divisible_num = n - divisible
       # print(f'divisible_num {divisible_num} and divisible {divisible}')
        if divisible == 0:
            return n
        elif (divisible_num % m) == 0:
           # print(f'output {n - divisible}')
            return n - divisible
    


# closestNumber(-6, 39);

def isBadVersion(version) -> bool:
    return version == 4

def firstBadVersion(n: int) -> int:
        start = 1
        end = n
        while start <= end:
            middle = (start + end)// 2
            if isBadVersion(middle):
                end = middle - 1
            else:
                start = middle + 1
        return start

print(firstBadVersion(5))
