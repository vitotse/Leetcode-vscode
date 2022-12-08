#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort(reverse=True)

        result = 0
        for i in range(len(g)):
            for j in range(len(s)-1, -1, -1):
                if s[j] >= g[i]:
                    
                    result += 1
                    del s[j]
                    break
                
                del s[j]

        return result

# @lc code=end

