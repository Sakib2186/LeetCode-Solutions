'''
Problem Statement:

You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

 

Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation:


In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

Example 2:

Input: board = [["X"]]

Output: [["X"]]


Problem Type: Medium

Problem Link: https://leetcode.com/problems/surrounded-regions/

'''

class Solution:
    def solve(self, board) -> None:
        
        top_row = 0
        bottom_row = len(board) - 1
        left = 0 
        right = len(board[0])
        visited = set()

        def bsf(i,j):

            queue = []
            queue.append((i,j))

            directions = [[0,1],[0,-1],[1,0],[-1,0]]

            while queue:
                r,c = queue.pop(0)
                board[r][c] = "T"
                for x,y in directions:

                    row = x + r
                    col = y + c

                    if row in range(bottom_row) and col in range(right) and board[row][col] == "O" and (row,col) not in visited:
                        visited.add((row,col))
                        queue.append((row,col))

        #top row
        for i in range(right):
            if board[top_row][i] == "O" and (top_row,i) not in visited:
                bsf(top_row,i)
        #bottom row
        for i in range(right):
            if board[bottom_row][i] == "O" and (bottom_row,i) not in visited:
                bsf(bottom_row,i)
        
        #first column
        for i in range(bottom_row):
            if board[i][left] == "O" and (i,left) not in visited:
                bsf(i,left)
        
        #last column
        for i in range(bottom_row):
            if board[i][right-1] == "O" and (i,right-1) not in visited:
                bsf(i,right-1)


        for i in range(bottom_row+1):
            for j in range(right):
                if board[i][j] == "T":
                    board[i][j]= "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"