from typing import List


def count_rotations_binary(nums):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if mid > 0 and nums[mid] < nums[mid - 1]:
            return mid
        elif nums[mid] < nums[high]:
            high = mid - 1
        else:
            low = mid + 1


nums = [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]
rotation_count = count_rotations_binary(nums)


# print("Rotation Count:", rotation_count)

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing
# a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# [7,1,5,3,6,4]
# prices is not sorted so we should use linear to go over all the days price
# declare two variable buy_price and sel_price.
# loop each day to choose lowest price to buy.
# loop each day to choose highest price to sell.

def maxProfit(self, prices: List[int]) -> int:
    min_price = float('inf')  # Stores the lowest price seen so far
    max_profit = 0  # Stores the max profit possible

    for price in prices:
        # Update min_price if we find a new lower price
        if price < min_price:
            min_price = price

        # Calculate profit if we sell on this day
        profits = price - min_price

        # Update max_profit if this profit is larger
        if profits > max_profit:
            max_profit = profits

    return max_profit


stocks = [1, 2]
profit = maxProfit(stocks, stocks)
# print(f'profit is {profit}')


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1.sort()
    nums2.sort()
    i, j = 0, 0
    result = []

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1  # Move pointer i
        elif nums1[i] > nums2[j]:
            j += 1  # Move pointer j
        else:  # nums1[i] == nums2[j]
            result.append(nums1[i])
            i += 1
            j += 1

    return result

result = intersect([1,2,2,1], [2])
print(f'result: {result}')

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        nums_dict = {}
        unique = 0
        for index in range(len(nums)):

            if nums[index] in nums_dict:
                count = nums_dict[nums[index]]
                nums_dict[nums[index]] = count + 1
            else:
                nums_dict[nums[index]] = 1

        for map_val in nums_dict.values():
            if map_val == 1:
                unique = map_val

        return unique

    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid_point = (low + high) // 2

            if nums[mid_point] == target:
                return mid_point

            if nums[mid_point] > target:
                high = mid_point - 1
            else:
                low = mid_point + 1
        return 0

