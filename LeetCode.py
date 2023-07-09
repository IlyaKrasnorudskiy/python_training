class Solution(object):
    def twoSum(nums, target):
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[i] + nums[j] == target:
                    if i !=j:
                        mas = [i, j]
                        return mas

print(Solution.twoSum([2,5,5,11],10))

class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        if x == x[::-1]:
            return True
        else:
            return False
