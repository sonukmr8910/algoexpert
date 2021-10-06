class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Time: O(n)
# Space: O(n)
def branch_sums(root):
    sums = []
    calculate_branch_sums(root, 0, sums)
    return sums


def calculate_branch_sums(node, currentSum, sums):
    if node is None:
        return

    currentSum += node.value
    if node.left is None and node.right is None:
        sums.append(currentSum)
        return

    calculate_branch_sums(node.left, currentSum, sums)
    calculate_branch_sums(node.right, currentSum, sums)
