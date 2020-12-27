class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        hashmap, t_map = {}, {}
        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = [i]
            else:
                hashmap[s[i]].append(i)

        for i in range(len(t)):
            if t[i] not in t_map:
                t_map[t[i]] = [i]
            else:
                t_map[t[i]].append(i)

        for values in hashmap.values():
            if values not in t_map.values():
                return False
        return True