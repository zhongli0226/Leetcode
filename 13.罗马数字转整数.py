#
# @lc app=leetcode.cn id=13 lang=python
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res = 0
        for i in range(len(s)):
            if i > 0 and dic[s[i]] > dic[s[i-1]]:
                res += dic[s[i]] - 2 * dic[s[i-1]]
            else:
                res += dic[s[i]]
        return res
# @lc code=end

