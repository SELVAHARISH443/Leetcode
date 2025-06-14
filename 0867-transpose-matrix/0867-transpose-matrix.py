class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        t=[]
        for i in range(0,len(matrix[0])):
            s=[]
            for j in range(0,len(matrix)):
                s.append(matrix[j][i])
            t.append(s)
        return t
        