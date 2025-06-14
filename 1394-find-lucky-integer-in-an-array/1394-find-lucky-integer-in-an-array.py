class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        c,max=-1,0
        for i in range(0,len(arr)):
            if arr.count(arr[i])==arr[i] and arr[i]>c:
                c=arr[i]
        return c
             

        