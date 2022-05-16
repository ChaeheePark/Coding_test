class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans=1
        if n%2==0:
            return (x**2)**(n/2)
        else:
            return x*(x**2)**((n-1)/2)
