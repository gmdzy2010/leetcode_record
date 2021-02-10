def get_max_area(height_list):
    left_index, right_index, max_area = 0, len(height_list) - 1, 0
    while left_index < right_index:
        width = right_index - left_index
        if height_list[left_index] < height_list[right_index]:
            height = height_list[left_index]
            left_index += 1
        else:
            height = height_list[right_index]
            right_index -= 1
        if max_area < width * height:
            max_area = width * height
    return max_area


if __name__ == '__main__':
    height_list = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    result = get_max_area(height_list)
    print(result)
