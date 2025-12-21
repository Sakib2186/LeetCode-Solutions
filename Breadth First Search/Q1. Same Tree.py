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
        
        stack = [(p,q)]

        while stack:
            node1,node2 = stack.pop()
            if node1 and node2:
                if node1.val != node2.val:
                    return False
            elif (node1 and not node2) or (not node1 and node2):
                return False
            
            if node1 and node2:
                stack.append((node1.left,node2.left))
                stack.append((node1.right,node2.right))

        return True