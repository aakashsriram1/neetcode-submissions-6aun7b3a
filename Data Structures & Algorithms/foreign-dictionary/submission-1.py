class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(list)
        indeg = {}
        for word in words:
            for c in word:
                indeg[c] = 0
                
        def compare(word1,word2):
            for i in range(min(len(word1), len(word2))):
                if word1[i] != word2[i]:
                    graph[word1[i]].append(word2[i])
                    indeg[word2[i]] += 1
                    break 
            if len(word1) > len(word2) and word1[:len(word2)] == word2: 
                return ""
            
        for i in range(len(words) - 1):
            if compare(words[i], words[i+1]) == "":
                return ""

        
        q = deque()
        for char,count in indeg.items():
            if count == 0:
                q.append(char)
        res = []
        while q: 
            char = q.popleft()
            res.append(char)
            for nei in graph[char]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
        
        if len(res) != len(indeg): 
            return ""
        else:
            return "".join(res)


      
      # hrn vs hrf 
        # steps 
            # find the first differing character 
            # that character will come before the other character in the dictionary 
            # so iterate throguh and here the difference is f so we know that comes first in dictionary 
            # so n -> f 

            # next example is hrf vs er 
            # so we know h and e are different 
            # so h -> e 

            # er vs enn
            # we know r -> n (we already have n -> f) so r -> n -> f 

            # enn vs rfnn 
            # e < f so 
            # e -> f  
            # summarize from before h -> e -> r -> n -> f




         