class Solution(object):
    def two_sum(self, nums, target):


        mydict = {}
        for i, num in enumerate(nums):
            complement = target - num


            if complement in mydict:
                return [mydict[complement],i]


            mydict[num] = i


        return []

solution = Solution()
nums = [2, 7, 11, 15]
target = 9
print(solution.two_sum(nums, target))  