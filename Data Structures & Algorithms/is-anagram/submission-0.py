class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_arr, t_arr = [i for i in s], [j for j in t]
        s_arr.sort()
        t_arr.sort()
        if s_arr == t_arr: 
            return True
        else: 
            return False
        