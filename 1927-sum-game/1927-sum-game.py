class Solution:
    def sumGame(self, num: str) -> bool:
        def stat(inp):  return reduce(
            lambda s,c: (s[0]+int(c),s[1]) if str.isdigit(c) else (s[0],s[1]+1), inp, initial=(0,0)
        )
        (ls,lm),(rs,rm) = stat(num[:len(num)//2]), stat(num[len(num)//2:])
        return (ls + 9*(am:= (lm+rm+1)//2) > rs + 9*rm) or (rs + 9*am > ls + 9*lm)
        