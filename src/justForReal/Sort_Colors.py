def sortColors(nums):
	start = 0;
	end = len(nums) - 1;
	i = 0;
	while (i <= end):
		if nums[i] == 0:
			nums[i]=1;
			nums[start]=0;
			start+=1
			i+=1
		elif nums[i] == 2:
			nums[i]=nums[end];
			nums[end]=2;
			end-=1
		else:
			i+=1
	return nums
	# """
	# :type nums: List[int]
	# :rtype: void Do not return anything, modify nums in-place instead.
	# """
	# i,j = 0,0
	# for index in range(len(nums)):
	# 	if nums[index] ==0:
	# 		swap(nums,i,index)
	# 		swap(nums,j,index)
	# 		i+=1
	# 		j+=1
	# 	if nums[index] ==1:
	# 		swap(nums,index,j)
	# 		j+=1
	# 	if nums[index] ==2:
	# 		continue
	# return nums




def swap(nums,i,j):
	temp = nums[i]
	nums[i] = nums[j]
	nums[j] = temp

nums = [0,1,2,0]
print(sortColors(nums))