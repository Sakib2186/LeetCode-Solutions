'''
Problem Statement:

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Problem Type: Medium

Problem Link: https://leetcode.com/problems/word-search/description/?envType=problem-list-v2&envId=array



'''
class Solution:
    def exist(self, board, word):
        rows, cols = len(board), len(board[0])

        def dfs(r, c, k):
            if k == len(word):
                return True

            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or 
                board[r][c] != word[k]):
                return False
            temp = board[r][c]
            board[r][c] = "#"

            found = (
                dfs(r+1, c, k+1) or
                dfs(r-1, c, k+1) or
                dfs(r, c+1, k+1) or
                dfs(r, c-1, k+1)
            )
            board[r][c] = temp

            return found

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False     