class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        r=[""]
        for i in range(len(digits)):
            t=[]
            for j in range(len(r)):
                for k in range(len(d[digits[i]])):
                    t.append(r[j]+d[digits[i]][k])
            r=t
        return r