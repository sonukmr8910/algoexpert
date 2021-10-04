# Time: O(nlog(n))
# Space: O(1)

def two_number_sum(array, targetSum):
    left = 0
    right = len(array) - 1
    array.sort()

    while left < right:
        sum = array[left] + array[right]
        if sum == targetSum:
            return [array[left], array[right]]
        elif sum < targetSum:
            left += 1
        elif sum > targetSum:
            right -= 1
    return []


# Test
# Expected: 12 and 62 sums to 74
array = [41, 64, 54, 37, 59, 62, 12]
targetSum = 74
nums = two_number_sum(array, targetSum)
if len(nums) == 2:
    print('{} and {} sums to {}'.format(nums[0], nums[1], targetSum))
else:
    print('Numbers not found')
