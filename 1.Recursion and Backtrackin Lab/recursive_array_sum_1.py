def calc_num(nums,idx):
    if idx == len(nums) - 1:
        return nums[idx]
    return nums[idx] + calc_num(nums, idx + 1)


nums = [int(x) for x in input().split()]

print(calc_num(nums, 0))
