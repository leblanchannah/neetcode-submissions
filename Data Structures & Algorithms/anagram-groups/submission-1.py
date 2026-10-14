class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for i, word in enumerate(strs):
            common_rep = ''.join(sorted(word))
            # if common_rep not in anagrams:
            #     anagrams[common_rep] = []
            anagrams[common_rep].append(word)
            
        return list(anagrams.values())
