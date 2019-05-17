
class Solution:
    def reOrderArray(self, array):
        # write code here
        if not array:
            return
        i,j = 0,len(array)-1
        while(i<j):
            while(i<j and self.check(array[i])):
                i+=1
            while(i<j and not self.check(array[i])):
                j-=1
            if i<j:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    def check(self,num):
        return (num&1)==1

    