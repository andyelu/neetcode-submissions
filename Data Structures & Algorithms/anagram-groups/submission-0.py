class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            # process letter counts
            curr_letter_counts = [0] * 26

            for ch in word:
                curr_letter_counts[ord(ch)-ord('a')] += 1

            curr_letter_counts = tuple(curr_letter_counts)
            
            # check if this array exists as a key already, if so we will increment the val
            if curr_letter_counts not in anagrams:
                anagrams[curr_letter_counts] = []
            anagrams[curr_letter_counts].append(word)

        return list(anagrams.values())
