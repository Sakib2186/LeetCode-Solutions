'''
Problem Statement:

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


Problem Type: Medium

Problem Link: https://leetcode.com/problems/number-of-islands/

'''

class Solution:
    def numIslands(self, grid) -> int:
        
        if not grid:
            return 0

        count = 0
        row = len(grid)
        column = len(grid[0])
        visited = set()

        def bfs(i,j):

            queue = []
            queue.append((i,j))
            directions = []

            while queue:

                #current iteration
                x,y = queue.pop(0)
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for r,c in directions:
                    #possible new coordinates
                    roo = x + r
                    coo = y + c

                    if roo in range(row) and coo in range(column) and grid[roo][coo] == "1" and (roo,coo) not in visited:
                        queue.append((roo,coo))
                        visited.add((roo,coo))
                        

        for i in range(0,row):
            for j in range(0,column):

                if grid[i][j] == "1" and (i,j) not in visited:
                    bfs(i,j)
                    count +=1

        return count

    

                

        

    
