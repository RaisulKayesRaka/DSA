# Binary Search

## Code
```python
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1
```

## Complexity
**Time Complexity:**
- Best case Complextiy: $$O(1)$$
- Average case Complextiy: $$O(logn)$$
- Worst case Complextiy: $$O(logn)$$
**Space Complexity:** $$O(1)$$