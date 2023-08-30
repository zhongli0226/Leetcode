#
# @lc app=leetcode.cn id=28 lang=python
#
# [28] 找出字符串中第一个匹配项的下标
#

# @lc code=start
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        if needle not in haystack:
            return -1
        else:
            return haystack.index(needle)
# @lc code=end

