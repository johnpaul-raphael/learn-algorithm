from typing import List


class TreeNode:

    def __init__(self, value=0):
        self.value = value
        self.left = None
        self.right = None


def insert_value_into_binary_tree(root, value):
    if not root:
        return TreeNode(value)
    if value < root.value:
        root.left = insert_value_into_binary_tree(root.left, value)
    else:
        root.right = insert_value_into_binary_tree(root.right, value)
    return root


def print_in_order(node):
    if not node:
        return
    print_in_order(node.left)
    print(node.value, end=' ')
    print_in_order(node.right)


# create binary search tree
root = None
values = [8, 3, 10, 1, 6, 14, 4, 7, 13]
for val in values:
    root = insert_value_into_binary_tree(root, val)
    # print(f"Tree after inserting {val}: ", end='')
    print_in_order(root)
    print()  # for a new line


def plusOne(digits: List[int]) -> List[int]:
    index = len(digits) - 1
    for digit in reversed(digits):
        if digit < 9:
            digits[index] = digits[index] + 1
            return digits
        else:
            digits[index] = 0
    digits = [0] * (len(digits) + 1)
    digits[0] = 1
    return digits


result = plusOne([9])
print(f'plus one result {result}')
