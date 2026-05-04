class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits:
            return []
        dictionary = {
            '2' : ['a','b','c'], 
            '3' : ['d','e','f'],
            '4' : ['g','h','i'],
            '5' : ['j','k','l'],
            '6' : ['m','n','o'],
            '7' : ['p','q','r','s'],
            '8' : ['t','u','v'],
            '9' : ['w','x','y','z']        
        }
        def backtrack(index,path):
            #if this path length is len(digits) then we got one valid path 
            if len(path) == len(digits):
                res.append("".join(path))
                return 
            
            for x in dictionary[digits[index]]:
                path.append(x)
                backtrack(index+1, path)
                path.pop()
        backtrack(0,[])
        return res
            

        
