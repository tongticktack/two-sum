from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    result = []
    for e in range(0, len(nums)):
        dif = target - nums[e]
        for ee in range(e + 1, len(nums)):
            if(nums[ee] == dif):
                result.append(e)
                result.append(ee)
                return result