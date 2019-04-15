class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        sequences = collections.defaultdict(int) #set '0' as the default value for non-existing keys
        for i in range(len(s)-9):
            sequences[s[i:i+10]] += 1#add 1 to the count
        return [key for key, value in sequences.iteritems() if value > 1]