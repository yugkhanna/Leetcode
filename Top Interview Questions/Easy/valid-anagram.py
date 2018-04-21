class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self,s,t):
        if(len(s)!=len(t)):
            return False

        count = {}

        for c in s:
            if (c.lower() in count):
                count[c.lower()] += 1
            else:
                count[c.lower()] = 1

        for c in t:
            if (c.lower() in count):
                count[c.lower()] -= 1
            else:
                count[c.lower()] = -1
            if count[c.lower()] < 0:
                return False

        return True

# Problem : https://leetcode.com/problems/valid-anagram/description/
