class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, t: int) -> int:
        c=0
        s=0
        for i in range(k):
            s+=arr[i]
        r=s/k
        if r>=t:
            c+=1
        for i in range(1,len(arr)-k+1):
            s-=arr[i-1]
            s+=arr[i+k-1]
            r=s/k
            if r>=t:
                c+=1
        return c