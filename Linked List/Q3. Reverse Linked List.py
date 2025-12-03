'''
Problem Statement:

Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 
Problem Type: Easy

Problem Link: https://leetcode.com/problems/reverse-linked-list/description/


'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head):

        if not head:
            return head
        
        prev = None
        curr = head

        while curr:
            node_ = ListNode(curr.val)
            if prev:
                node_.next = prev
            prev = node_
            curr = curr.next
        return node_