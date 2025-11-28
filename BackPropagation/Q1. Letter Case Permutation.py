'''
Problem Statement:

Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.

 

Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: s = "3z4"
Output: ["3z4","3Z4"]
 
Problem Type: Medium

Problem link: https://leetcode.com/problems/letter-case-permutation/description/


'''

class Solution:
    def letterCasePermutation(self, s: str):
        
        output = [""]

        for c in s:
            temp = []
            if c.isalpha():
                for o in output:
                    temp.append(o+c.lower())
                    temp.append(o+c.upper())

            else:
                for o in output:
                    temp.append(o+c)
            output = temp

        return output