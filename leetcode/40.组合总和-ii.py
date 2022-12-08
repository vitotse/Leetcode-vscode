#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        size = len(candidates)
        if size == 0:
            return []
        res = []
        
        candidates.sort()

        def dfs(begin, path, remain):
            
            if remain == 0:
                res.append(path[:])
                return

            for i in range(begin, size):
                
                if candidates[i] > remain:
                    break
                
                if i > begin and candidates[i] == candidates[i-1]:
                    continue
               
                path.append(candidates[i])
                
                dfs(i+1, path, remain-candidates[i])
                
                path.pop()

        dfs(0, [], target)
        return res


# @lc code=end

