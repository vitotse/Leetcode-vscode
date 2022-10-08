#
# @lc app=leetcode.cn id=953 lang=python3
#
# [953] 验证外星语词典
#

# @lc code=start
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapping = dict()
        for i, c in enumerate(order):
            mapping[c] = i
        decrypt = []
        for word in words:
            decrypt.append("".join([chr(ord('a') + mapping[c]) for c in word]))     
        return decrypt == sorted(decrypt)

# @lc code=end

