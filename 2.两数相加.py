#
# @lc app=leetcode.cn id=2 lang=python
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 初始化一个虚拟节点作为结果链表的头结点  
        dummy = ListNode()  
        # 初始化一个指针指向结果链表的尾结点  
        tail = dummy  
        # 初始化进位值  
        carry = 0  
        # 遍历两个链表，逐位相加  
        while l1 or l2 or carry:  
            # 获取两个链表当前位的值，以及进位值  
            x = l1.val if l1 else 0  
            y = l2.val if l2 else 0  
            # 计算当前位的和以及新的进位值  
            sum = x + y + carry  
            carry = sum // 10  
            sum %= 10  
            # 将当前位的和添加到结果链表的尾部  
            tail.next = ListNode(sum)  
            tail = tail.next  
            # 移动指针到下一个位置  
            if l1:  
                l1 = l1.next  
            if l2:  
                l2 = l2.next  
        # 返回结果链表的头结点  
        return dummy.next

# @lc code=end

