class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []
            
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}        

        res = []

        def backtrack(combi, digits):
            if not digits:
                res.append(combi)
                return
            
            for letter in letters[digits[0]]:
                backtrack(combi+letter, digits[1:])
        
        backtrack("", digits)
        return res