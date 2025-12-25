'''
Problem Statement:

Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.

 

Example 1:


Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
Example 2:


Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-104 <= Node.val <= 104
root is guaranteed to be a valid binary search tree.
-105 <= k <= 105

Problem Type: Easy

Problem Link: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/


'''
from collections import deque

class Solution:
    def findTarget(self, root, k: int) -> bool:

        queue = deque()
        queue.append(root)
        visited = set()
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if k - node.val in visited:
                    return True
                visited.add(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        
        return False