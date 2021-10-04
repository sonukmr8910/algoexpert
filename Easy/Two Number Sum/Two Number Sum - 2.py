# Time: O(n)
# Space: O(n)

def two_number_sum(array, targetSum):
    nums = {}
    for i in range(len(array) - 1):
        potentialNum = targetSum - array[i]
        if potentialNum in nums:
            return [potentialNum, array[i]]
        nums[array[i]] = True
    return []


# Test
# Expected: 9 and 2 sums to 11
array = [1, -4, 5, 7, 9, 2, 12]
targetSum = 11
nums = two_number_sum(array, targetSum)
if len(nums) == 2:
    print('{} and {} sums to {}'.format(nums[0], nums[1], targetSum))
else:
    print('Numbers not found')
