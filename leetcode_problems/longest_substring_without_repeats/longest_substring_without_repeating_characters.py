class Solution(object):
    # First attempt, shitty brute force
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in range(len(s)):
            char_dict = {}



if __name__ == "__main__":
    string = 'test'
    sol = Solution()
    length = sol.lengthOfLongestSubstring(string)
    print length
