#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ans = []

        def helper(start, path, target):
            if len(path) > k or target < 0:
                return

            if target == 0:
                if len(path) == k:
                    ans.append(path[:])
                    return
                else:
                    return

            for i in range(start, 9):
                path.append(candidates[i])
                target -= candidates[i]
                helper(i + 1, path, target)
                path.pop()
                target += candidates[i]

        helper(0, [], n)
        return ans

# @lc code=end

