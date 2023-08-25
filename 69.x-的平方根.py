#
# @lc app=leetcode.cn id=69 lang=python
#
# [69] x 的平方根 
#

# @lc code=start
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        t, q, r = 0, 0, x
        N = len(bin(x)[2:])
        while N:
            N -= 1
            t = 2 * q + (1 << N)
            if (r >> N) >= t:
                r -= (t << N)
                q += (1 << N)
        return q
# @lc code=end

