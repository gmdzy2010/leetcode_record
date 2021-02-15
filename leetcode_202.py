def get_sum(n):
    result = 0
    while n:
        result += (n % 10) * (n % 10)
        n //= 10
    return result


def is_happy_number_hash_set(n):
    sum_set = set()
    while True:
        result = get_sum(n)
        if result == 1:
            return True
        if result in sum_set:
            return False
        else:
            sum_set.add(result)
        n = result


def is_happy_number_double_pointer(n):
    slow = get_sum(n)
    fast = get_sum(get_sum(n))
    while slow != fast:
        slow = get_sum(slow)
        fast = get_sum(get_sum(fast))
    return slow == 1


if __name__ == '__main__':
    # result = is_happy_number_hash_set(19)
    test_result = is_happy_number_double_pointer(19)
    print(test_result)
