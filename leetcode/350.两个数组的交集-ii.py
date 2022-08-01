#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        n = len(nums1)

        res=[]

        index = 0
        for target in nums2: 
            if index == n:  
                break
            left = index
            right = n - 1
            # 二分查找
            while left < right:
                mid = left + (right - left) // 2
                if nums1[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            # nums2中的元素在nums1中找到了下一次二分查找的左边界就加一
            # 没找到下一次二分查找的左边界就还是现在的左边界
            if nums1[left] == target:
                index = left + 1     
                res.append(target)
        return res


# @lc code=end

