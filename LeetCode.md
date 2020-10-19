## LeetCode

- 两数之和：





~~~python
class Solution:
	def twoSum(self,nums,target):
		n = len(nums) # 获取nums的长度，是4
		for x in range(n): # 外层循环先取出下标0，对应着数组里的第一个数字
			for y in range(x+1,n): # 内层循环取出下标1，对应着数组里的第二个数字
				if nums[x] + nums[y] == target: # 如果第一个数字+第二个数字=target
					return x,y # 上面的判断是对的话，那么就返回下标
					break # 并停止程序
				else: # 如果上面的条件不满足的话，内层for循环就会继续取出下标2进行判断...如果都不满足，那么外层for循环就会取出下标1...依次类推
					continue 
~~~

~~~python
class Solution:
	def twoSum(self,nums,target):
		n = len(nums)
		for x in range(n):
			a = target - nums[x]
			if a in nums: # 判断a有没有在nums数组里
				y = nums.index(a) # 有的话，那么用index获取到该数字的下标
				if x == y: 
					continue # 同样的数字不能重复用，所以这里如果是一样的数字，那么就不满足条件，跳过
				else: # 否则就返回结果
					return x,y 
					break
			else: 
				continue # 上面的条件都不满足就跳过，进行下一次循环


~~~

~~~python
class Solution:
	def twoSum(self,nums,target):
		d = {} #空字典
		n = len(nums)
		for x in range(n):
			d[nums[x]] = x # 把数组里的数字作为key，下标作为value存到d字典中
			if target - nums[x] in d: # 看另外一个数字有没有在字典里
				return d[target-nums[x]],x # 有的话直接就可以返回value了;没有的话会继续循环

~~~

~~~python
class Solution:
	def twoSum(self,nums,target):
		d = {}
		n = len(nums)
		for x in range(n):
			if target - nums[x] in d:
				return d[target-nums[x]],x
			else:
				d[nums[x]] = x

~~~

