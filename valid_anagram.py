class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        HM = {}
        if len(s) != len(t):
            return False
        for each in s:
            if each in HM:
                HM[each] += 1
            else:
                HM[each] = 1
        for each in t:
            if each in HM:
                HM[each] -= 1
            else:
                return False
        for val in HM:
            if HM[val] != 0:
                return False
        return True