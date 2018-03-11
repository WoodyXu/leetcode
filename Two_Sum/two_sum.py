import numpy as np

# first solution O(n^2)
def two_sum(nums, target):
    arr_len = len(nums)
    for i in range(arr_len):
        for j in range(i + 1, arr_len):
            if nums[i] + nums[j] == target:
                return [i, j]

# second solution O(n)
def two_sum2(nums, target):
    sorted_idxes = np.argsort(nums)
    sorted_nums = np.array(nums)[sorted_idxes]
    i, j = 0, len(sorted_nums) - 1
    while i < j:
        if sorted_nums[i] + sorted_nums[j] == target:
            return [ sorted_idxes[i], sorted_idxes[j] ]
        elif sroted_nums[i] + sorted_nums[j] > target:
            j -= 1
        else:
            i += 1

# third solution O(n)
def two_sum3(nums, target):
    value_idx_d = dict()
    for i in range(len(nums)):
        residual = target - nums[i]
        if residual in value_idx_d:
            return [ value_idx_d[residual], i ]
        else:
            value_idx_d[nums[i]] = i

if __name__ == "__main__":
    nums = [3, 2, 4]
    target = 6
    assert two_sum(nums, target) == [1, 2]
    assert two_sum2(nums, target) == [1, 2]
    assert two_sum3(nums, target) == [1, 2]
