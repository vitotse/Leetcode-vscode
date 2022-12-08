#
# @lc app=leetcode.cn id=491 lang=python3
#
# [491] 递增子序列
#

# @lc code=start
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        def dfs(i, tmp):
            if i == len(nums):
                if len(tmp) >= 2:
                    res.append(tmp[:])      # 拷贝，tmp[:]而非tmp
                return
            
            # 选 nums[i]
            if not tmp or nums[i]>=tmp[-1]: # 需满足递增
                tmp.append(nums[i])         # 选nums[i]
                dfs(i+1, tmp)
                tmp.pop()                   # 回溯复原
                # dfs(i+1, tmp+[nums[i]])   # 与以上三行等价
            
            # 不选 nums[i]：
            # 只有在nums[i]不等于前一项tmp[-1]的情况下才考虑不选nums[i]
            # 即若nums[i] == tmp[-1]，则必考虑选nums[i]，不予执行不选nums[i]的情况
            if not tmp or (tmp and nums[i] != tmp[-1]): # 避免重复
                dfs(i+1, tmp)


        res = []
        dfs(0, [])
        return res

# @lc code=end

