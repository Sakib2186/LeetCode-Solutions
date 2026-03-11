'''
Problem Statement:


 

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
 

Constraints:

0 <= n <= 5 * 106

Problem Type: Medium

Problem Link: https://leetcode.com/problems/count-primes/description/



'''

class Solution:
    def countPrimes(self, n: int) -> int:

        def find_prime(num):

            for i in range(2,(num//2)+1):
                if i != num and num%i == 0:
                    return False
            return True

        count = 0 
        for i in range(2,n):
            if find_prime(i):
                count += 1
        return count

        