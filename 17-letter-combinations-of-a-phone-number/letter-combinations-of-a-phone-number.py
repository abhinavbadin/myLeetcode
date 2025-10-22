class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        kmap = {
            "2" : ["a","b","c"],
            "3" : ["d","e","f"],
            "4" : ["g","h","i"],
            "5" : ["j","k","l"],
            "6" : ["m","n","o"],
            "7" : ["p","q","r","s"],
            "8" : ["t","u","v"],
            "9" : ["w","x","y","z"]
        } 
        res = []

        def backtrack(index,path):
            if index == len(digits):
                res.append(path)
                return

            letters = kmap[digits[index]]
            
            for ch in letters:
                backtrack(index+1,path+ch)

        backtrack(0,"")
        return res