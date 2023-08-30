'''
Description: 
Version: 
Autor: tangwc
Date: 2023-08-30 21:35:11
LastEditors: tangwc
LastEditTime: 2023-08-30 21:41:27
FilePath: \Leetcode\67.二进制求和.py

 Copyright (c) 2023 by tangwc, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=67 lang=python
#
# [67] 二进制求和
#

# @lc code=start
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a,2)+int(b,2))[2:]
# @lc code=end

