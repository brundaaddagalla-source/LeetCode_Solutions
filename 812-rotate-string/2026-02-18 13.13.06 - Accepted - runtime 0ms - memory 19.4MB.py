class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return (False)
            exit(0)
        s=list(s)
        for i in range(len(s)):
            if s[i:]+s[:i]==list(goal):
                return (True)
                exit(0)
        return False
        