#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原 IP 地址
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(cur_ans: str, p: int, add_num: int):
            assert 0 <= p <= n, 'p should within [0, n]'
            if p == n and add_num == 4:
                ans.append(cur_ans)
            elif p == n or add_num == 4:
                return
            else:
                if add_num > 0: cur_ans += '.' # 加‘.’
                backtrack(cur_ans + s[p], p + 1, add_num + 1) # 取一位数
                if p <= n - 2 and s[p] != '0': # 取两位数
                    backtrack(cur_ans + s[p:p+2], p + 2, add_num + 1)
                if p <= n - 3 and s[p] != '0' and int(s[p:p+3]) <= 255: # 取三位数
                    backtrack(cur_ans + s[p:p+3], p + 3, add_num + 1)
        
        n, ans = len(s), []
        backtrack('', 0, 0)
        return ans


# @lc code=end

