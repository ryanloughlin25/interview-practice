"""This is bad, can probably do better with a hash map, two or one pass, but
what to do about repeated keys?"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for ind1, num1 in enumerate(nums):
            for ind2, num2 in enumerate(nums[ind1+1:]):
                if num1 + num2 == target:
                    return [ind1, (ind2+ind1+1)]

if __name__ == "__main__":
    nums = [3,2,4]
    target = 6
    sol = Solution()
    ret = sol.twoSum(nums, target)
    print ret
