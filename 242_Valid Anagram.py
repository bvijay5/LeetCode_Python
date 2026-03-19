class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dicts = {}
        dictt = {}
        for chs in s:
            dicts[chs] = dicts.get(chs, 0) +1

        for cht in t:
            dictt[cht] = dictt.get(cht, 0) +1
        return dicts == dictt