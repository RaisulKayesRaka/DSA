# Coin Change (Greedy Approach)

```python
def greedy_coin_change(coins, amount):
    coins.sort(reverse=True)
    change = []
    for coin in coins:
        count = amount // coin
        change.extend([coin] * count)
        amount %= coin

    if amount == 0:
        return change
    else:
        return None


coins = [3, 5, 10, 25]
amount = 37

change = greedy_coin_change(coins, amount)
if change:
    print(f"Change for {amount}: {change}")
else:
    print(f"No solution found for {amount}")
```
