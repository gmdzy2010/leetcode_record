def find_median_sorted_arrays(nums1, nums2):
    """The efficiency of version below is fairly enough, but NOT the best."""
    nums1.extend(nums2)
    nums1.sort()
    length = len(nums1)
    if length % 2 == 0:
        return (nums1[int(length / 2) - 1] + nums1[int(length / 2)]) / 2
    else:
        return nums1[int(length / 2)]


if __name__ == '__main__':
    nums_1, nums_2 = [1, 3, 5, 7], [2, 3, 4]
    result = find_median_sorted_arrays(nums_1, nums_2)
    print(result)
