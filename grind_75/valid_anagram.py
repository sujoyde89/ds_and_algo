class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        dic_s, dic_t = {}, {}
        for i in range(len(s)):
            dic_s[s[i]] = dic_s.get(s[i], 0) + 1
            dic_t[t[i]] = dic_t.get(t[i], 0) + 1

        for c in dic_s:
            if c not in dic_t or dic_s[c]!=dic_t[c]:
                return False
        return True
