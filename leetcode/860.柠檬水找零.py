#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#

# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic = {5:0,10:0,20:0}
        if bills[0] > 5:
            return False
        for bill in bills:
            if bill == 5:
                dic[5] += 1
            else:
                if bill == 10:
                    if dic[5] <= 0:return False
                    dic[5] -= 1
                    dic[10] += 1
                elif bill == 20:
                    if dic[5] <= 0:return False
                    if dic[10] > 0:
                        dic[10] -= 1
                        dic[5] -= 1
                    else:
                        if dic[5] >= 3:
                            dic[5] -= 3
                        else:
                            return False
                    dic[20] += 1
        return True

# @lc code=end

