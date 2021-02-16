def can_construct_standard_lib(ransom, magazine):
    magazine_characters = list(magazine)
    try:
        for character in ransom:
            magazine_characters.remove(character)
        return True
    except ValueError:
        return False


def can_construct_direct(ransom, magazine):
    ransom_characters, magazine_characters = list(ransom), list(magazine)
    for character_m in magazine_characters:
        for character_r in ransom_characters:
            if character_m == character_r:
                ransom_characters.remove(character_r)
    return True if len(ransom) == 0 else False


def can_construct_hash_array(ransom, magazine):
    record = [0] * 26
    ransom_length, magazine_length = len(ransom), len(magazine)
    for index in range(magazine_length):
        record[ord(magazine[index]) - 97] += 1
    for index in range(ransom_length):
        record[ord(ransom[index]) - 97] -= 1
        if record[ord(ransom[index]) - 97] < 0:
            return False
    return True


if __name__ == '__main__':
    test_ransom, test_magazine = 'aa', 'aab'
    # result = can_construct_standard_lib(test_ransom, test_magazine)
    # result = can_construct_direct(test_ransom, test_magazine)
    result = can_construct_hash_array(test_ransom, test_magazine)
    print(result)
