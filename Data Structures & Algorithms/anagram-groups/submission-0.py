class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for wrd in strs:
            bank = [0] * 26
            for char in wrd: 
                bank[ord(char) - ord('a')] += 1 
            hashmap[tuple(bank)].append(wrd)
        return list(hashmap.values())