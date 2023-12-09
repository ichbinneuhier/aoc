def predict(nums):
    if not any(nums):
        return 0
    new = [None for i in range(len(nums)-1)]
    for i in range(len(nums)):
        try:
            new[i] = nums[i+1] - nums[i]
        except:
            pass
    return nums[0]-predict(new)

with open("aoc-9-input.txt") as f:
    final = 0
    for line in f:
        line = line.strip()
        nums = list(map(int, line.split()))
        final += predict(nums)
    print(final)