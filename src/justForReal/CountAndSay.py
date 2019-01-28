#problem 38

def countAndSay(self, n):
	s = '1'
	for _ in range(n - 1):
		let, temp, count = s[0], '', 0
		for l in s:
			if let == l:
				count += 1
			else:
				temp += str(count) + let
				let = l
				count = 1
		temp += str(count) + let
		s = temp
	return s


# def countAndSay(n):
# 	"""
# 	:type n: int
# 	:rtype: str
# 	"""
# 	output = str(1)
# 	count = 0
# 	before = 1
# 	output = "1"
# 	if n==1:
# 		return "1"
# 	for _ in range(1,n):
# 		count = 0
# 		before = 0
# 		for i in range(len(output)):
# 			new_output = ""
# 			if int(output[i]) == before and i!=len(output)-1:
# 				count +=1
# 			elif int(output[i]) == before and i==len(output)-1:
# 				count += 1
# 				new_output += (str(count) + str(before))
# 			elif int(output[i]) != before and i == len(output) - 1:
# 				new_output += (str(count) + str(before))
# 				new_output += (str(1) + str(output[i]))
# 			else:
# 				new_output+=(str(count)+str(before))
# 				before = int(output[i])
# 				count = 1
# 		output = new_output
# 	return  output
# print(countAndSay(5))