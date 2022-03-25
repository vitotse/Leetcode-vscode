#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # 按下限排序
        intervals.sort(key=lambda x : x[0])

        merged = []

        for interval in intervals:
            # merged 为空，或者 当前区间下限与merged不重合
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 重合时，下限用最大值
                merged[-1][1] = max(merged[-1][1], interval[1])


        return merged

# @lc code=end

