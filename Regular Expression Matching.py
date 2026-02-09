def isMatch(s: str, p: str) -> bool:
    # DP table
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

    # Empty string & empty pattern match
    dp[0][0] = True

    # Handle patterns like a*, a*b*, a*b*c*
    for j in range(2, len(p) + 1):
        if p[j - 1] == "*":
            dp[0][j] = dp[0][j - 2]

    # Fill DP table
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):

            # Case 1: direct match or '.'
            if p[j - 1] == s[i - 1] or p[j - 1] == ".":
                dp[i][j] = dp[i - 1][j - 1]

            # Case 2: '*'
            elif p[j - 1] == "*":
                # Treat * as zero occurrence
                dp[i][j] = dp[i][j - 2]

                # If previous char matches
                if p[j - 2] == s[i - 1] or p[j - 2] == ".":
                    dp[i][j] = dp[i][j] or dp[i - 1][j]

    return dp[len(s)][len(p)]


# 🔹 Test Examples
print(isMatch("aab", "c*a*b"))   # True
print(isMatch("aa", "a"))        # False
print(isMatch("ab", ".*"))       # True
print(isMatch("mississippi", "mis*is*p*."))  # False
