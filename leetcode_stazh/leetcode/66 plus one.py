class Solution(object):
    def plusOne(self, digits):
        return [int(digit) for digit in str(int("".join(map(str,digits)))+1)]

obj = Solution()
arr = [1,2,3]
print(obj.plusOne(arr))
