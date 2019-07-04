#22  DFS
class Solution(object):
	def generateParenthesis(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""
		if not n:
			return []
		left, right, ans = n, n, []
		self.dfs(left, right, ans, "")
		return ans

	def dfs(self, left, right, ans, string):
		if right < left:
			return
		if not left and not right:
			ans.append(string)
			return
		if left:
			self.dfs(left - 1, right, ans, string + '(')
		if right:
			self.dfs(left, right - 1, ans, string + ')')

#2 solution
class Solution(object):
	def generateParenthesis(self, n):
		"""
        :type n: int
        :rtype: List[str]
        """
		res = []
		self.part("(", 1, 0, n, res)
		return res

	def part(self, pre, a, b, n, res):
		if n == a and a == b:
			res.append(pre)
		else:
			if n > a:
				self.part(pre + "(", a + 1, b, n, res)
			if a > b:
				self.part(pre + ")", a, b + 1, n, res)


