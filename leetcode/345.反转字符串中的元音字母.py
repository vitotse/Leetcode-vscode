#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = "aeiouAEIOU"
        # 双指针
        left, right = 0, len(s) - 1
        s = list(s)
        while left < right:
            while s[left] not in vowel and left < right:
                left += 1
            while s[right] not in vowel and left < right:
                right -= 1
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return "".join(s)

# @lc code=end

