class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        '''
        write = 0

        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write], nums[read] = nums[read], nums[write]
                write += 1
'''     
        l=[]
        c=0
        for i in nums:
            if i!=0:
                l.append(i)
            else:
                c+=1
        for i in range(c):
            l.append(0)
        for i in range(len(l)):
            nums[i]=l[i]