#
# @lc app=leetcode.cn id=1232 lang=python3
#
# [1232] 缀点成线
#

# @lc code=start
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        vec = [None, None]
        for p1, p2 in pairwise(coordinates):
            if vec[0] is None:
                vec[0] = p2[0] - p1[0]
                vec[1] = p2[1] - p1[1]
            else:
                if vec[0] * (p2[1] - p1[1]) != vec[1] * (p2[0] - p1[0]):
                    return False
        return True






# @lc code=end

