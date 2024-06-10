# Fractional Knapsack

```python
def fractional_knapsack(weights, values, capacity):
    items = sorted(zip(weights, values),
                   key=lambda x: x[1] / x[0], reverse=True)
    knapsack = []
    weight = 0
    value = 0
    for w, v in items:
        if weight + w <= capacity:
            knapsack.append((w, v))
            weight += w
            value += v
    return knapsack, value


weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
knapsack, total_value = fractional_knapsack(weights, values, capacity)

print("Selected items:", knapsack)  # Selected items: [(10, 60), (20, 100)]
print("Total value:", total_value)  # Total value: 160
```