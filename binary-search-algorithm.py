# QUESTION 1: Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card.

# brute force approach

#1. create a variable as initial = 0, mid_point = cards//2, end_val = len(cards)
#2. check if midpoint index equals to expected value if yes then return it
#3. if no match found then check if expected value is greater or less
#4. if the value is greater then end_val = mid_point -1
#5. if the value is lesser than initial = mid_point +1

# Binary Search Algorithm
#----------------------------------------------------------
#A binary search algorithm is a search technique that efficiently finds a target value within a sorted array by repeatedly dividing the search space in half, comparing the target value to the middle element, and then narrowing the search to either the lower or upper half based on the comparison, until the target is found or the search space is exhausted; it is considered a "divide and conquer" algorithm. 
# user case
# works well with sorted array
#----------------------------------------------------------

cards = [9,8,7,6,5,4,3,2,1]
query = 6

def locate_card(cards, query):
    start = 0
    end = len(cards) -1
    while start <= end:
        mid = (start + end)//2
        if(cards[mid] == query):
            return mid
        elif(cards[mid] > query):
            start =mid+1
        elif(cards[mid] < query):
            end = mid-1
        
    return -1
    
result = locate_card(cards, query)    
print(f"the result is: {result}")