## 66.加一

~~~
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。
~~~

> 思路：想象成小学生练习加法，只不过现在是固定的“加一”那么我们只需要考虑如何通过遍历来实现这个加法的过程就好了。

> 加法我们知道要从低位到高位进行运算，那么只需要对数组进行一次反向遍历即可。

~~~java
# 伪代码
for(int i = n - 1; i > - 1; i --) {
  内部逻辑
}
~~~

~~~ python
# 三种可能的情况
1. 个位上的数字小于9
    17
+   1
= 18 //将数组的最后一位进行+1 操作
2. 个位数上等于9，其他位数可以是0-9的任何数，但是首位不等于9
    199
+     1
=  200
//把个位的 carry 向前进一位并在计算是否有更多的进位
    109
+      1
=  110
3. 所有位数都为9
    99
+    1
= 100

      999
+       1
=  1000
//扩大数组的长度  在结果数组前多加上一位



# 伪代码
// 首先我们要从数组的最后一位开始我们的计算得出我们新的sum
sum = arr[arr.length - 1] + 1

// 接下来我们需要判断这个新的sum是否超过9
sum > 9 ?

// 假如大于 9, 那么我们会更新这一位为 0 并且将carry值更改为1
carry = 1
arr[i] = 0

// 假如不大于 9，更新最后一位为sum并直接返回数组
arr[arr.length - 1] = sum
return arr

// 接着我们要继续向数组的倒数第二位重复进行我们上一步的操作
...

// 当我们完成以后，如果数组第一位时的sum大于0，那么我们就要给数组的首位增添一个1
result = new array with size of arr.length + 1
result[0] = 1
result[1] ...... result[result.length - 1]  = 0 //
~~~

~~~python
// 官方题解
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i], carry = (carry + digits[i]) % 10, (carry + digits[i]) // 10
        return [carry] + digits if carry else digits
~~~

~~~python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] is not 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
                if digits[0] is 0:
                    digits.insert(0, 1)
                    return digits
~~~

