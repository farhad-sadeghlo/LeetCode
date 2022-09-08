class twoSum:
    def __init__(self, nums: list[int], target: int) -> list[int]:
        self.nums = list(map(int, nums.rstrip().split()))
        self.target = int(target)
    def twoSum(self):
        for i, num in enumerate(self.nums):
            rem = self.target - self.nums[i]
            if rem in self.nums and num != rem:
                return print(self.nums.index(num), self.nums.index(rem))
            elif num == rem and target == 2 * num and self.nums.count(num) >= 2:
                return print([i for i, num in enumerate(self.nums) if self.nums.count(num) >= 2])