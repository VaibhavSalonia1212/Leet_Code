class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
            # Odd length palindrome
            p1 = expand_around_center(i, i)
            # Even length palindrome
            p2 = expand_around_center(i, i + 1)
            
            # Choose the longer one
            if len(p1) > len(longest):
                longest = p1
            if len(p2) > len(longest):
                longest = p2
        
        return longest
