"""
回文数：
回文数：从正序和倒序读都一样的整数

思路：
1. 利用python切片一行搞定(内存消耗大)

2.位运算？
 
....


"""

class Solution:
    def isPalindrome1(self, x: int) -> bool:
        return str(x) == str(x)[::-1]



    def isPalindrome2(self, x: int) -> bool:



