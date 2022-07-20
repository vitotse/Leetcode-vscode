#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        a=len(needle)
        b=len(haystack)
        if a==0:
            return 0
        i=j=0
        next=self.getNext(a,needle)
        while(i<b and j<a):
            if j==-1 or needle[j]==haystack[i]:
                i+=1
                j+=1
            else:
                j=next[j]
        if j==a:
            return i-j
        else:
            return -1

    def getNext(self,a,needle):
        next=['' for i in range(a)]
        j,k=0,-1
        next[0]=k
        while(j<a-1):
            if k==-1 or needle[k]==needle[j]:
                k+=1
                j+=1
                next[j]=k
            else:
                k=next[k]
        return next

# @lc code=end

