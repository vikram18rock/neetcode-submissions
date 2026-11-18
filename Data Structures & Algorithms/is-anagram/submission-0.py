class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # each letter frequency should match with other word
        sFreq = defaultdict(int)
        tFreq = defaultdict(int)
        for letter in range(26):
            for i in range(len(s)):
                if (chr(letter + ord('a'))) == s[i] :
                    sFreq[letter] += 1
            for j in range(len(t)):
                if (chr(letter + ord('a'))) == t[j] :
                    tFreq[letter] += 1
        if sFreq == tFreq :
            return True
        return False
        # check frequencies in s
        # check frequencies in t

        # check if both match and return