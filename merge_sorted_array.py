def merge(nums1, m, nums2, n):
    last = m + n - 1
    i = m - 1  # Last element in the m part of nums1
    j = n - 1  # Last element in nums2
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[last] = nums1[i]
            i -= 1
        else:
            nums1[last] = nums2[j]
            j -= 1
        last -= 1
    while j >= 0:
        nums1[last] = nums2[j]
        j -= 1
        last -= 1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)  # Output: [1,2,2,3,5,6]
