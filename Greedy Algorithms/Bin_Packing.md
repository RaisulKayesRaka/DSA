# Bin Packing

```python
def bin_packing(items, bin_capacity):
    bins = []
    for item in items:
        assigned = False
        for bin in bins:
            if item <= bin_capacity - sum(bin):
                bin.append(item)
                assigned = True
                break
        if not assigned:
            bins.append([item])

    return bins


items = [10, 5, 12, 3, 8, 7, 4]
bin_capacity = 15

packed_bins = bin_packing(items, bin_capacity)
# Packed bins: [[10, 5], [12, 3], [8, 7], [4]]
print(f"Packed bins: {packed_bins}")
print(len(packed_bins))
```
