class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i=0
        j=1
        l=[]
        c=1
        if len(nums)==0:
            return []
        if len(nums)==1:
            return [f"{nums[-1]}"]
        while i<len(nums) and j<len(nums):
            if nums[i]+c==nums[j]:
                j+=1
                c+=1
            elif j-i<2:
                l.append(str(f"{nums[i]}"))
                c=1
                i=j
                j+=1

                
            else:
                l.append(str(f"{nums[i]}->{nums[j-1]}"))
                i=j
                c=1
                j+=1
        if j-i<2:
            l.append(str(f"{nums[i]}"))
        else:
            l.append(str(f"{nums[i]}->{nums[j-1]}"))
        return l