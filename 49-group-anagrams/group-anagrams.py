from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for string in strs:
            key = ''.join(sorted(string.lower()))
            hashmap[key].append(string)
        return list(hashmap.values())