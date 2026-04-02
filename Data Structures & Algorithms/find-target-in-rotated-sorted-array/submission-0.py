class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min_index = self.find_min(nums)

        if self.is_on_right(nums, target):
            return self.binary_search(nums, target, min_index, len(nums) - 1)
        else:
            return self.binary_search(nums, target, 0, min_index - 1)

    def is_on_right(self, nums: List[int], target: int) -> bool:
        return target <= nums[-1]

    def binary_search(self, nums: List[int], target: int, left: int, right: int) -> int:
        if left > right:
            return -1

        lo = left - 1
        hi = right

        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] >= target:
                hi = mid
            else:
                lo = mid

        return hi if nums[hi] == target else -1

    def find_min(self, nums: List[int]) -> int:
        lo = -1
        hi = len(nums) - 1

        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] <= nums[-1]:
                hi = mid
            else:
                lo = mid

        return hi