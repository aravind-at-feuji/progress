# leet code 49.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ditn : dict[str, list] = {}
        for i in range(len(strs)) :
            st = sorted(strs[i])
            st = str(st)
            if st in ditn :
                t = ditn.get(st)
                t.append(strs[i])
            else :
                t = []
                t.append(strs[i])
                ditn[st] = t
        res = []
        for key, val in ditn.items() :
            res.append(val)
        return res

        