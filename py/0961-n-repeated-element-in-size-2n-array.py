import collections
from typing import Dict, List


# solution with two dicts
# would also be possible to do with just num_ct if, after the for loop, we chek all keys to find the key with value n
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        ct_num: Dict[int, List[int]] = collections.defaultdict(list)
        num_ct: Dict[int, int] = collections.defaultdict(int)
        for i in nums:
            try:
                ct_num[num_ct[i]].pop(i)
            except:
                pass
            num_ct[i] += 1
            ct_num[num_ct[i]].append(i)
        n = len(num_ct.keys()) - 1
        return ct_num[n][0]
