'''
Problem Statement:

Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

 

Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
 

Constraints:

1 <= s.length <= 5 * 105
s consists of uppercase and lowercase English letters and digits.
 

Problem Type: Medium

Problem Link: https://leetcode.com/problems/sort-characters-by-frequency/description/?envType=problem-list-v2&envId=heap-priority-queue


'''
import heapq
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:

        list_of_chars = list(s)
        list_of_chars = Counter(list_of_chars)
        max_heap = []
        for key,value in list_of_chars.items():
            heapq.heappush(max_heap,(-value,key))

        result_string = ""
        while max_heap:
            value,key = heapq.heappop(max_heap)
            while value != 0:
                result_string += key
                value += 1
        return result_string
        