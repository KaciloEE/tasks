﻿class Solution(object):	
	def fizzBuzz(self, n):
		self.n = n
		l = []
		for i in range(1,self.n+1):			
			if (i%3==0) and (i%5==0):				
				l.append('FizzBuzz')
			elif (i%3==0):
				l.append("Fizz")
			elif (i%5==0):
				l.append("Buzz")
			else:
				l.append(str(i))
	
		return l

		
print(Solution().fizzBuzz(15))

def fizzBuzz(self, n):
    return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]