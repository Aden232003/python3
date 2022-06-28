from re import X


x1=121
x2=-121

class Solution():
    def __init__(self,x):
        self.x = x
    @staticmethod
    def isPalindrome(x:int):
        string = str(x)
        invStr = string[::-1]
        if invStr != string:
            return False
        return True


print(Solution.isPalindrome(x1))
print(Solution.isPalindrome(x2))