from typing import List


def selection_sort(arr: List[int | float]) -> List[int | float]:
    if len(arr) == 1:
        return arr

    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


if __name__ == "__main__":
    arr = [4, 1, 3, 5, 6, 8, 9, 2, 7]
    print(selection_sort(arr))
