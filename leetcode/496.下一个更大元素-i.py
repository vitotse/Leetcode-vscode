#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = deque()
        larger_dict = {}
        for value in nums2[::-1]:
            while stack and stack[-1] <= value:
                stack.pop()
            
            larger_dict[value] = stack[-1] if stack and stack[-1] > value else -1
            stack.append(value)

        return [larger_dict[v] for v in nums1]

# @lc code=end

