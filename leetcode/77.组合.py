#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def back_tracking(start,temp):
            if len(temp) == k:                      # 符合条件，将组合添加到结果
                res.append(temp[:])
                return
            for i in range(start, n+1):
                if (n+1-start + len(temp)) < k:     # 当前所能组成的最大长度组合已经小于K时，则直接return，不符合要求
                    return
                temp.append(i)
                back_tracking(i+1, temp)
                temp.pop()
        back_tracking(1, [])
        return res

# @lc code=end

