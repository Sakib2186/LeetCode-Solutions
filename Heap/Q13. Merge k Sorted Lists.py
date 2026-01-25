'''
Problem Statement:

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Problem Type: Hard

Problem Link: https://leetcode.com/problems/merge-k-sorted-lists/

'''

import heapq
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        min_heap = []
        for l in lists:
            head = l
            curr = head
            while curr!=None:
                heapq.heappush(min_heap,curr.val)
                curr = curr.next

        head = None
        prev = None
        while len(min_heap)!=0:
            element = heapq.heappop(min_heap)
            curr = ListNode(val=element)
            if not head:
                head = curr
                prev = curr
            else:
                prev.next = curr
                prev=curr
        return head

        