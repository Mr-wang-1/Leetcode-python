# 数组返回 不同项

"""
思路1：
1. 调用collections函数中的Counter方法  可以分别对t 和 s 计数  找出不同项
2. list()强转
3. 返回列表项
耗时久  内存消耗大


思路2：
位运算:
1.先用for遍历字符串中的字符
2.ord函数对其解码
3.对其异或运算
4.chr()函数可以反向得出字符
"""

import collections

class Solution:

    def findTheDifference(self, s: str, t: str) -> str:
        return list((collections.Counter(t)-collections.Counter(s)).elements())[0]

solution = Solution()     #实例化对象   对象调用方法  类实例化对象 
t =['a', 'b', 'c', 'd']   
s=['d', 'b', 'c', 'e', 'a']
print(solution.findTheDifference(t,s))






class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = 0
        for i in s:
            ans ^= ord(i)

        for i in t:
             ans ^= ord(i)
        
        return chr(ans)
