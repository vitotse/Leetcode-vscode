#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 翻转字符串里的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        cur = ""
        for ch in s:
            if ch == " ":
                if cur:
                    words.append(cur)
                    cur = ""
            else:
                cur += ch

        if cur:
            words.append(cur)

        for i in range(len(words) // 2):
            words[i], words[len(words) - 1 - i] = words[len(words) - 1 - i], words[i]
        
        return " ".join(words)
# @lc code=end

