import copy
class Solution(object):
	def combine(self, n, k):
		"""
		:type n: int
		:type k: int
		:rtype: List[List[int]]
		"""
		results = []
		result = []

		def DFS(results, result, start, n, k):
			if (k == len(result)):
				results.append(copy.deepcopy(result))  # python append()与深拷贝、浅拷贝应该注意，此处有一个大坑
				return
			for i in range(start, n + 1, 1):
				result.append(i)
				DFS(results, result, i + 1, n, k)
				result.pop()

		DFS(results, result, 1, n, k)
		return results