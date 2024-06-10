# Linear Search

## Code
```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
```

## Complexity
**Time Complexity:** $$O(n^2)$$
**Space Complexity:** $$O(1)$$