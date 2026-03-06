
#Concatenation of Array 😌

class Solution(object):
  def getConcatenation(self, nums):
    n=len(nums)
    ans = []
    for i in range(n):
      ans.append(nums[i])
    for i in range(n):
      ans.append(nums[i])
    return ans
# Main Program Starts Here
nums = list(map(int,input().split()))
obj = Solution()
result = obj.getConcatenation(nums)
print(result)