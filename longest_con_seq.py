# T: O(n)  S: O(n)
def longestConsecutive(nums):
    num_set = set(nums)
    best = 0

    for n in num_set:
        # only start a count if n is the beginning of a sequence
        if (n - 1) not in num_set:
            length = 1
            while (n + length) in num_set:
                length += 1
            best = max(best, length)

    return best