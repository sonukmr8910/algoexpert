# Average: O(log(n)) time | O(1) space
# Worst: O(n) time | O(1) space

def find_closest_in_bst(tree, target):
    closest = float('inf')
    currentNode = tree
    while currentNode is not None:
        if abs(target - currentNode.value) < abs(target - closest):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest
