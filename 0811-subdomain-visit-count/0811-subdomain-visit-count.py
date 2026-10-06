class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        r=[]
        d={}
        for i in cpdomains:
            c,domain=i.split()
            print(c,domain)
            domains=domain.split(".")
            print(domains)
            for j in range(len(domains)):
                s=(".").join(domains[j:])
                d[s]=d.get(s, 0)+int(c)
        print(d)
        for i in d:
            r.append(str(d[i])+" "+i)
        return r
            