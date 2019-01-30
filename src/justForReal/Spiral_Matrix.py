matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

ret = []
while matrix:
	ret += matrix.pop(0)
	if matrix and matrix[0]:
		for row in matrix:
			ret.append(row.pop())
	if matrix:
		ret += matrix.pop()[::-1]
	if matrix and matrix[0]:
		for row in matrix[::-1]:
			ret.append(row.pop(0))

print(ret)

# temp = matrix = [
#  [ 4, 5 ],
#  [ 7, 8 ]
# ]
#
# print(temp.pop()[::-1])