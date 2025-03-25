class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(num):
            total = 0
            while num > 0:
                digit = num % 10
                total += digit ** 2 
                num //= 10  
            return total
        s = set() 
        while n != 1 and n not in s:
            s.add(n)
            n = get_next(n)
        return n == 1  
