class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram={}
        for word in strs:
            sortedword = "".join(sorted(word))
            if sortedword in anagram:
                anagram[sortedword].append(word)
            else:
                anagram[sortedword]=[word]
                
        return list(anagram.values())
        