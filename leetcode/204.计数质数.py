#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#

# @lc code=start
class Solution:
    
    def countPrimes(self, n: int) -> int:
        # 最小的质数是 2
        if n < 2:
            return 0

        isPrime = [1] * n
        isPrime[0] = isPrime[1] = 0   # 0和1不是质数，先排除掉

        # 埃式筛，把不大于根号 n 的所有质数的倍数剔除
        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i]:
                isPrime[i * i:n:i] = [0] * ((n - 1 - i * i) // i + 1)

        return sum(isPrime)



# @lc code=end

