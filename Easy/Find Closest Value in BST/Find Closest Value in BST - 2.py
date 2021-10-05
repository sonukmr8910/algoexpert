# Average: O(log(n)) time | O(log(n)) space
# Worst: O(n) time | O(n) space

def find_closest_in_bst(tree, target, closest=float("inf")):
    return find_closest_in_bst_helper(tree, target, closest)


def find_closest_in_bst_helper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - tree.value) < abs(target - closest):
        closest = tree.value
    if target < tree.value:
        return find_closest_in_bst_helper(tree.left, target, closest)
    elif target > tree.value:
        return find_closest_in_bst_helper(tree.right, target, closest)
    else:
        return closest
