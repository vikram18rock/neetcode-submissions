class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupedAnagrams = dict(list())
        for s in strs :
            head = "".join(sorted(s))
            if head not in groupedAnagrams:
                groupedAnagrams[head] = []
            groupedAnagrams[head].append(s)
        return list(groupedAnagrams.values())