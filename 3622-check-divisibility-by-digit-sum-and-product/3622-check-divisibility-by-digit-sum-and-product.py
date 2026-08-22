class Solution:
    def checkDivisibility(self, n: int) -> bool:
        n_str=str(n)
        prod=1
        Sum=0
        for i in n_str:
            prod*=int(i)
            Sum+=int(i)
        return n%(prod+Sum)==0
        