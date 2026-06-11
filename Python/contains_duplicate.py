class duplicates:

    def __init__(self, nums):

        self.nums = list(map(int, nums.rstrip().split()))

    def containsDuplicate(self):

        dup_num = None

        nums = sorted(self.nums)

        for num in nums:

            if dup_num != num:

                dup_num = num

            elif dup_num == num:

                return print(True)

            else:

                return print(False)
