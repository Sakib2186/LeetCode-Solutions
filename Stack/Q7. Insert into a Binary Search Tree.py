'''
Problem Statement:

You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

 

Example 1:


Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
Explanation: Another accepted tree is:

Example 2:

Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]
Example 3:

Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]
 
Problem Type: Medium

Problem Link: https://leetcode.com/problems/insert-into-a-binary-search-tree/description/




'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root, val: int):

        stack = [root]
        while stack:

            node = stack.pop()
            if node:
                if node.val < val:
                    if node.right:
                        stack.append(node.right)
                    else:
                        temp = TreeNode(val)
                        node.right = temp
                        return root
                else:
                    if node.left:
                        stack.append(node.left)
                    else:
                        temp = TreeNode(val)
                        node.left = temp
                        return root
            else:
                temp = TreeNode(val)
                root = temp
                return root
        
# Time Complexity : O(lg2)