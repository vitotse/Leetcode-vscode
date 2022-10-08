#
# @lc app=leetcode.cn id=1376 lang=python3
#
# [1376] 通知所有员工所需的时间
#

# @lc code=start
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        dct = defaultdict(list)
        for i in range(n):
            dct[manager[i]].append(i)

        def dfs(pre, root):
            nonlocal ans
            if not dct[root]:
                if pre > ans:
                    ans = pre
                return
            for nex in dct[root]:
                dfs(pre+informTime[root], nex)
            return

        ans = 0
        dfs(0, headID)
        return ans

# @lc code=end

