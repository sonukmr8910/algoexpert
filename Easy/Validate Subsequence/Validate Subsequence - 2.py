# Time: O(n)
# Space: O(1)

def validate_subsequence(array, sequence):
    seqIdx = 0
    for item in array:
        if seqIdx == len(sequence):
            break
        if item == sequence[seqIdx]:
            seqIdx += 1
    return seqIdx == len(sequence)


# Test
# Expected: True
array = [84, 23, 34, 76, 34]
sequence = [84, 76]
print(validate_subsequence(array, sequence))
