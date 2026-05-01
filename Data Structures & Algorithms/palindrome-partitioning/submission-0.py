class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(index,path):
            if index == len(s):
                res.append(path[:])
                return

            for end in range(index + 1, len(s) + 1):
                piece = s[index:end]

                if is_palindrome(piece):
                    path.append(piece)
                    backtrack(end,path)
                    path.pop()

        backtrack(0,[])
        return res
