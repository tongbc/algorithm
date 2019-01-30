#55 junmp game
def canJump(self, nums):
	"""
	:type nums: List[int]
	:rtype: bool
	"""
	m = 0
	for index, n in enumerate(nums):
		if index > m:
			return False
		m = max(m, index + n)
	return True