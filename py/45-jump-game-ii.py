"""
45. Jump Game II
by Alex JPS
2023-02-07

This is a rough draft,
This code works but is WILDLY inefficient right now.
"""

def do_jump(nums: list[int], start: int = 0):
    assert len(nums) >= 1, "there are no items in nums!"
    
    # base cases
    if start == len(nums) - 1:
        # at win condition
        return 0
    elif start not in range(len(nums)):
        # out of bounds
        print("start is out of bounds")
        return None
    elif nums[start] <= 0:
        # cannot make jumps
        print("cannot make jumps")
        return None

    # recursive case
    print(f"recur case nums[{start}] = {nums[start]}")
    min = None
    for k in range(1, nums[start] + 1):
        if start + k >= len(nums):
            break
        current = do_jump(nums, start + k)
        if current is None:
            # path does not work
            continue
        elif min is None:
            # take first valid path
            min = current
        elif current < min:
            # take shortest path
            min = current
    if min is None:
        # no valid paths from here
        print(f"no valid paths from nums[{start}] = {nums[start]}")
        return None
    else:
        # return min jumps + jump we're making here
        return 1 + min

nums = [5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2,7,9,7,9,6,9,4,1,6,8,8,4,4,2,0,3,8,5]
print(do_jump(nums, 0))