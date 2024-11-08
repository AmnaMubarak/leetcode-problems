class Solution:
  def containsDuplicate(self, nums):
    
    hashset = set()
    for i in nums:
      if i in hashset:
        return True
      hashset.add(i)
    
    return False  
  
  
obj = Solution()
nums = [1,1,1,3,3,4,3,2,4,2]
print(obj.containsDuplicate(nums))  