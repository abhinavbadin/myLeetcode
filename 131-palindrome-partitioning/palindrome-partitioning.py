class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_palindrome(string):
            if string == string[::-1]:
                return True
            return False

        def backtrack(index,path):
            if index == len(s):
                res.append(path[:])
                return 
            
            for st in range(index, len(s)):
                substring = s[index:st+1]
                if is_palindrome(substring):
                    path.append(substring)
                    backtrack(st+1,path)
                    path.pop()
        backtrack(0,[])
        return res 