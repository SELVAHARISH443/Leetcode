class Solution:
    def checkRecord(self, s: str) -> bool:
        t=list(s)
        c=0
        l=0
        for i in t:
            if(i=='A' or i=='a'):
                c=c+1
           
        if c>=2:
            return False
        elif "LLL" in s:
            return False
        else:
            return True

            
            