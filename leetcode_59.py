def generate_matrix(n):
    level, start, width = 0, 0, n
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    while width > 0:
        if width == 1:
            center_x = center_y = len(matrix) // 2
            matrix[center_x][center_y] = len(matrix) ** 2
            return matrix
        
        direction = [
            (0, 1, (0 + level, 0 + level)),
            (1, 0, (0 + level, width - 1 + level)),
            (0, -1, (width - 1 + level, width - 1 + level)),
            (-1, 0, (width - 1 + level, 0 + level))
        ]
        for number in range(4):
            step_x, step_y, init = direction[number]
            for inc in range(width - 1):
                dimension_x = init[0] + step_x * inc
                dimension_y = init[1] + step_y * inc
                filled_number = number * (width - 1) + inc + 1 + start
                matrix[dimension_x][dimension_y] = filled_number
        level, start, width = level + 1, start + 4 * (width - 1), width - 2
    
    return matrix


if __name__ == '__main__':
    result = generate_matrix(6)
    print(result)
