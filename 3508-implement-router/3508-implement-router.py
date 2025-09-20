from collections import deque
class Router:
    def __init__(self, memoryLimit: int):
        self.n=memoryLimit
        self.dis=defaultdict(lambda: deque())
        self.packages=deque()
        self.exist=defaultdict(int)
    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if(self.exist[(source,destination,timestamp)]):
            return False
        if(len(self.packages)==self.n):
            s,d,t=self.packages.popleft()
            self.exist[(s,d,t)]=0
            self.dis[d].popleft()
        self.exist[(source,destination,timestamp)]=1
        self.dis[destination].append(timestamp)
        self.packages.append((source,destination,timestamp))
        return True
    def forwardPacket(self) -> List[int]:
        if not(self.packages):
            return []
        s,d,t=self.packages.popleft()
        self.exist[(s,d,t)]=0
        self.dis[d].popleft()
        return [s,d,t]
    def getCount(self, d: int, s: int, e: int) -> int:
        low,high=0,len(self.dis[d])-1
        a=-1
        while(low<=high):
            mid=low+(high-low)//2
            if(self.dis[d][mid]>=s):
                a=mid
                high=mid-1
            else:
                low=mid+1
        if(a==-1 or  not (s<=self.dis[d][a]<=e)):
            return 0
        low,high=a,len(self.dis[d])-1
        b=a
        while(low<=high):
            mid=low+(high-low)//2
            if(self.dis[d][mid]<=e):
                b=mid
                low=mid+1
            else:
                high=mid-1
        return b-a+1