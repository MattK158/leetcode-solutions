# T: O(n)  S: O(n)  — bucket sort approach
def topKFrequent(nums, k):
    count = {}
    for n in nums:
        count[n] = count.get(n, 0) + 1

    # bucket[i] = list of numbers that appear i times
    freq = [[] for _ in range(len(nums) + 1)]
    for num, cnt in count.items():
        freq[cnt].append(num)

    res = []
    for i in range(len(freq) - 1, 0, -1):  # iterate high freq -> low
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res