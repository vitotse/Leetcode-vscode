#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        numDict = dict()
        for num in nums:
            if num in numDict:
                return True
            else:
                numDict[num] = num
        
        return False

# @lc code=end

