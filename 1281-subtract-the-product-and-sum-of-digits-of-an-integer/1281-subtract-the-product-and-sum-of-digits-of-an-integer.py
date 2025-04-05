class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p=1
        s=0
        for i in str(n):
            t=int(i)
            p=p*t
            s=s+t
        return p-s