from typing import List


def main(nums: List[int]) -> List[int]:
    size = len(nums)
    if not size or size < 2:
        return nums

    process(nums, 0, size - 1)

    return nums


def process(nums: List[int], L: int, R: int):
    if L < R:
        P = partition(nums, L, R)
        process(nums, L, P - 1)
        process(nums, P + 1, R)


def partition(nums: List[int], L: int, R: int) -> int:
    pivot = nums[R]
    P = L - 1
    for i in range(L, R):
        if nums[i] <= pivot:
            P += 1
            nums[i], nums[P] = nums[P], nums[i]

    nums[P + 1], nums[R] = nums[R], nums[P + 1]

    return P + 1


if __name__ == "__main__":
    input_arr = [2, 1, 3, 5, 4, 7, 9, 8, 6, 6, 6]
    print(main(input_arr))
