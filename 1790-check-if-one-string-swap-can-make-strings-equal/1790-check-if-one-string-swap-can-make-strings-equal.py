class Solution(object):
    def areAlmostEqual(self, s1, s2):
        if s1 == s2:
            return True
        temp = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                temp.append(i)
        if len(temp) != 2:
            return False
        i, j = temp
        return s1[i] == s2[j] and s1[j] == s2[i]
