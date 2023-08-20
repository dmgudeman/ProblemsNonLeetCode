


# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):

        anas = defaultdict(list)
        for str in strs:
            dKey = tuple(sorted(str))
            anas[dKey].append(str)

        return anas.values()
