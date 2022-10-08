#
# @lc app=leetcode.cn id=1779 lang=python3
#
# [1779] 找到最近的有相同 X 或 Y 坐标的点
#

# @lc code=start
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_idx = -1
        min_distance = float('+inf')
        for i in range(len(points)):
            dx, dy = x - points[i][0], y - points[i][1]
            if dx * dy == 0 and abs(dx + dy) < min_distance:
                min_distance = abs(dx + dy)
                min_idx = i
        return min_idx


# @lc code=end

