class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_checker = {}
        grouped = []
        for i, n in enumerate(strs): 
            curr = "".join(str(char) for char in sorted(n)) 
            if curr in anagram_checker: 
                anagram_checker[curr].append(n)
            else: 
                anagram_checker[curr] = [n]
        
        for i in anagram_checker:
            grouped.append(anagram_checker[i])
        
        return grouped
        