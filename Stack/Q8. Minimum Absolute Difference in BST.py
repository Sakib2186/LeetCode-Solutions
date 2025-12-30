'''
Problem Statement:

Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

 

Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 104].
0 <= Node.val <= 105

Problem Type: Easy

Problem Link: https://leetcode.com/problems/minimum-absolute-difference-in-bst/


'''
from collections import deque
class Solution:
    
    def getMinimumDifference(self, root) -> int:

        queue = deque()
        queue.append(root)
        result = float('inf')

        stack = [root]

        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    result = min(result,abs(node.val-node.left.val))
                    queue.append(node.left)
                if node.right:
                    result = min(result,abs(node.val-node.right.val))
                    queue.append(node.right)
                print(result)

        while stack:
            node = stack.pop()
            if node.left:
                result = min(result,abs(node.val-node.left.val))
                stack.append(node.left)
            if node.right:
                result = min(result,abs(node.val-node.right.val))
                stack.append(node.right)
        
        return result

#solution not correct, will try again on own
