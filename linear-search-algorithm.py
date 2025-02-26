# QUESTION 1: Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card.

# brute force approach

#1. create a variable position as 0
#2. check if card position index contains expected value
#3. if yes then return the index
#4. if no match found then increment the position by 1 and repeat 2 to 3 until reaches end of cards.
#5. if position reaches the end and no match found then return -1

# Linear Search Algorithm
#----------------------------------------------------------
#Linear search, also known as sequential search, is a method for finding a target value within a list. It operates by examining each element in the list one by one, in sequential order, until either a match is found or the end of the list is reached. If the target value is found, the search typically returns the index of the element. If the target value is not in the list, the search may return a specific value (e.g., -1) or raise an exception to indicate that the element was not found.
# user case
# works well un-sorted array
#----------------------------------------------------------

cards = [9,8,7,6,5,4,3,2]
query = 6

def locate_card(cards, query):
    position = 0
    while (position < len(cards)):
        if(cards[position] == query):
            return position
        
        position += 1
        
    return -1
    
result = locate_card(cards, query)    
print(f"the result is: {result}")