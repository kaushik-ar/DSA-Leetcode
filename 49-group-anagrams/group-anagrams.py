from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        result = []
        for string in strs:
            key = ''.join(sorted(string.lower()))
            hashmap[key].append(string)
        for key in hashmap:
            result.append(hashmap[key])
        return result


        