# Time: O(n^2)
# Space: O(1)

def two_number_sum(array, targetSum):
    for i in range(len(array) - 1):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == targetSum:
                return [array[i], array[j]]
    return []


# Test
# Expected: -4 and 9 sums to 5
array = [1, -4, 5, 7, 9, 2, 12]
targetSum = 5
nums = two_number_sum(array, targetSum)
if len(nums) == 2:
    print('{} and {} sums to {}'.format(nums[0], nums[1], targetSum))
else:
    print('Numbers not found')
