class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        s=[]
        for i in image:
            i=[1 if x==0 else 0 for x in i]
            s.append(list(i[::-1]))
        return s

        