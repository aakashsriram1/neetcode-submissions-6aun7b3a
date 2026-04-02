class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # replacements = len of current string - most frequent character 
        # if this is > k then its valid 

        res = 0 
        l = r = 0 
        hashmap = defaultdict()

        while r < len(s): 
            hashmap[s[r]] = hashmap.get(s[r],0) + 1
            
            while len(s[l:r+1]) - max(hashmap.values()) > k:
                hashmap[s[l]] -= 1 
                if hashmap[s[l]] == 0: 
                    del  hashmap[s[l]]
                l = l + 1 

            res = max(res,r-l+1)
            r = r + 1 
                
            
        return res