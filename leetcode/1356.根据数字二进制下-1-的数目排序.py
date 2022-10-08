#
# @lc app=leetcode.cn id=1356 lang=python3
#
# [1356] 根据数字二进制下 1 的数目排序
#

# @lc code=start
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # 排序
        arr.sort()
        # 保存到字典中
        maxs = 0
        dict1 = {}
        for i in range(len(arr)):
            maxs = max(maxs, bin(arr[i]).count("1"))
            dict1[i] = bin(arr[i]).count("1")
        # 遍历字典
        res = []
        for i in range(0, maxs + 1):
            for k, v in dict1.items():
                if i == v:
                    res.append(arr[k])
        return res



# @lc code=end

