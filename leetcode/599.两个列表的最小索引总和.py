#
# @lc app=leetcode.cn id=599 lang=python3
#
# [599] 两个列表的最小索引总和
#

# @lc code=start
from cmath import inf


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        # list1 创建哈希表
        index = {s: i for i, s in enumerate(list1)}
        ans = []
        index_sum = inf

        # list2 找到 list1 相同的数值
        for i, s in enumerate(list2):
            if s in index:
                j = index[s]
                if i + j < index_sum:
                    index_sum = i + j
                    ans = [s]
                elif i + j == index_sum:
                    ans.append(s)
        return ans

# @lc code=end

