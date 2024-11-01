# Merge Sorted Array

https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        last = m + n - 1
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m = m - 1
            else:
                nums1[last] = nums2[n - 1]
                n = n - 1
            last = last - 1

        while n > 0:
            nums1[last] = nums2[n - 1]
            n = n - 1
            last = last - 1
```

> Time Complexity: `O(m + n)`

> Space Complexity: `O(1)`
