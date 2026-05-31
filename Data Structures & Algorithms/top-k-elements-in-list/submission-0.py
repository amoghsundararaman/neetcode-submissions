class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = {}

        for i in nums: 
            if i in freqDict: 
                freqDict[i] +=1
            else:
                freqDict[i] = 1
        
        frequencies = [i for i in freqDict.values()]

        frequencies.sort()

        frequencies = frequencies[-k:]

        res = []
        for i in freqDict: 
            if freqDict[i] in frequencies: 
                res.append(i)
        return res

        

        