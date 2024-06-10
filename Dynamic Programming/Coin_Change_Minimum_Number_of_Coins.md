# Coin Change: Minimum Number of Coins

```python
def coin_change_minimum_coins(coins, amount):
    m = len(coins)
    n = amount

    dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]

    # Initialize the first row with 0
    for i in range(m + 1):
        dp[i][0] = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if coins[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = min(dp[i - 1][j], 1 + dp[i][j - coins[i - 1]])

    return dp[m][n]
```