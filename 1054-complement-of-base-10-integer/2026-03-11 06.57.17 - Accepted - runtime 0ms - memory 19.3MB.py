class Solution:
    def bitwiseComplement(self, n: int) -> int:
        bin_original=bin(n)[2:]
        bin_com=""
        for i in bin_original:
            if i=='0': bin_com+='1'
            elif i=='1': bin_com+='0'
        com=int(bin_com,2)
        return com