# Time: O(n)
# Space: O(1)

def validate_subsequence(array, sequence):
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(sequence)


# Test
# Expected: True
array = [1, 3, 53, 7, 45, 78, 21]
sequence = [3, 7, 78]
print(validate_subsequence(array, sequence))
