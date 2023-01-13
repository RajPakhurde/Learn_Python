def removeDuplicates(nums):
    unique = []
    for item in nums:
        if item not in unique:
            unique.append(item)

    length = len(unique)
    return unique


result = removeDuplicates([1, 1, 2])
print(result)
