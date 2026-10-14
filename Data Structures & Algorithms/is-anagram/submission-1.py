class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_ctr = {}
        t_ctr = {}
        for i in s:
            if i not in s_ctr:
                s_ctr[i] = 0
            s_ctr[i] += 1
        for j in t:
            if j not in s_ctr:
                return False
            if j not in t_ctr:
                t_ctr[j] = 0
            t_ctr[j] += 1
            if len(s_ctr)<len(t_ctr):
                return False
        
        for si in s_ctr.keys():
            if si not in t_ctr.keys():
                return False
            if s_ctr[si]!=t_ctr[si]:
                return False

        return True

