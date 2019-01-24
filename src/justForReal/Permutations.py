class Solution(object):
	def permute(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		res = []
		lev, avail, lev_node = 0, nums, []
		N = len(nums)

		def dfs(lev, avail, lev_node):
			if lev == N:
				res.append(lev_node)
				return
			for i in range(len(avail)):
				dfs(lev + 1, avail[:i] + avail[i + 1:], lev_node + [avail[i]])

		dfs(lev, avail, lev_node)
		return (res)