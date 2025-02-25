def longestSubarray(nums):
    count = 0
    maxs = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
            if count > maxs:
                maxs = count
        else:
            count = 0
    return maxs

print(longestSubarray([1,1,1,0,1]))