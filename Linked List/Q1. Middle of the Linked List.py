'''

Problem Statement:

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.


Problem Type: Easy

Problem Link: https://leetcode.com/problems/middle-of-the-linked-list/description/


'''

class Solution:
    def middleNode(self, head):


        def lengthOfLinkedList():
            current = head
            count = 0
            while current:
                count += 1
                current = current.next
            return count

        number_of_nodes = lengthOfLinkedList()
        middle_index = (number_of_nodes)//2

        i =0
        current = head
        while i != middle_index:
            current = current.next
            i += 1

        return current
