#Longest palindromic sequence
def longestPalindromicSequence(s):

    for i in s:

        for j in s:

            if s[i] == s[j]:
                s[i][j] = s[i+1][j-1] + 2
            else:
                s[i][j] = max(s[i+1][j], s[i][j-1])
