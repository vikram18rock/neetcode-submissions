class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFrequency = {}
        for num in nums:
            numFrequency[num] = numFrequency.get(num, 0) + 1

        freqSortedNums = sorted(numFrequency.keys(), key=lambda x: numFrequency[x])

        return freqSortedNums[-k:]
