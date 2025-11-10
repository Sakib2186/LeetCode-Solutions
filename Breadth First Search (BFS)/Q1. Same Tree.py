'''

Problem Statement:

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Input: p = [1,2,3], q = [1,2,3]
Output: true

Input: p = [1,2], q = [1,null,2]
Output: false

Problem type: Easy

Problem link: https://leetcode.com/problems/same-tree/

'''

class Solution:
    def isSameTree(self, p, q) -> bool:
        
        if not p and not q:
            return True
        
        if p and q and p.val == q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        
        return False