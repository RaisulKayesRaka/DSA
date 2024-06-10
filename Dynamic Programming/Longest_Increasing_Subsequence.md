# Longest Increasing Subsequence

```python
def longest_increasing_subsequence(sequence):
    n = len(sequence)
    # dp[i] represents the length of the longest increasing subsequence ending at index i
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if sequence[i] > sequence[j]:
                dp[i] = max(dp[i], dp[j]+1)

    return max(dp)
```