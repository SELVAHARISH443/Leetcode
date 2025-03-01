class Solution:
    def reverseWords(self, s: str) -> str:
        lst1=s.split()
        rev=lst1[::-1]
        return ' '.join(rev)