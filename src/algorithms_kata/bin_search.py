

def bin_search(needle, haystack):
    left_index = 0
    right_index = len(haystack) - 1

    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2

        if haystack[middle_index] == needle:
            return middle_index

        if haystack[middle_index] > needle:
            right_index = middle_index - 1
        else:
            left_index = middle_index + 1

    return None


def bin_search_demo():
    print('Binary search')
    haystack = [1, 2, 13, 35, 56, 87, 89, 121, 143, 176, 221, 445, 866, 1122]
    needle = 35
    needle_index = bin_search(needle, haystack)
    print(haystack)
    print('needle:', needle)
    print('needle_index:', needle_index)
