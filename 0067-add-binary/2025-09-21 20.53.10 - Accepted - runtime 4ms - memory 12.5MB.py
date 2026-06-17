class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i=len(a)-1
        j=len(b)-1
        c=0
        r=[]
        while i>=0 or j>=0 or c:
            t=c
            if i>=0:
                t+=int(a[i])
                i-=1
            if j>=0:
                t+=int(b[j])
                j-=1
            r.append(str(t%2))
            c=t//2
        return ''.join(reversed(r))