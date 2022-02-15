#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answers = list()
        length = len(nums)
        if length < 3: return []

        for first in range(length):

            if first > 0 and nums[first] == nums[first - 1]:
                continue
            
            third = length - 1

            target = -nums[first]

            for second in range(first + 1, length):
                if second > first + 1 and nums[second]== nums[second - 1]:
                    continue

                while second < third and nums[second] + nums[third] > target:
                    third -= 1

                if second == third:
                    break

                if nums[second] + nums[third] == target:
                    answers.append([nums[first],nums[second], nums[third]])

        return answers

# @lc code=end

