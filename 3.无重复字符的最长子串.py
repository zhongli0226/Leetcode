#
# @lc app=leetcode.cn id=3 lang=python
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 记录字符上一次减去的下标
        dic = {}
        res = 0
        start = 0
        for i, c in enumerate(s):
            if c in dic:
                start = max(start, dic[c] + 1)
            dic[c] = i
            res = max(res, i - start + 1)
        return res
# @lc code=end

