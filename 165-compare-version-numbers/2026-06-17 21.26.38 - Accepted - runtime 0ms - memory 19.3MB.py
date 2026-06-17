class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1=version1.split(".")
        version2=version2.split(".")
        version1=[int(i) for i in version1]
        version2=[int(i) for i in version2]
        diff=abs(len(version2)-len(version1))
        if len(version2)>len(version1):
            version1.extend([0]*diff)
        else:
            version2.extend([0]*diff)
        for i in range(len(version1)):
            if version1[i]<version2[i]:
                return -1
            elif version1[i]>version2[i]:
                return 1
            else:
                continue
        return 0