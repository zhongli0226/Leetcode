#
# @lc app=leetcode.cn id=14 lang=python
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        strs.sort()
        for i in range(len(strs[0])):
            if strs[0][i] != strs[-1][i]:
                return strs[0][:i]
        return strs[0]
# @lc code=end

