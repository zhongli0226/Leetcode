#
# @lc app=leetcode.cn id=9 lang=python
#
# [9] 回文数
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        digits = str(x)
        left, right = 0, len(digits) - 1
        while left < right:
            if digits[left] != digits[right]:
                return False
            left += 1
            right -= 1
        return True

# @lc code=end

