def removeDuplicates(nums: list[int]) -> int:
  if not nums:
    return 0

  k = 1  # Unique elements ka index tracker
  for i in range(1, len(nums)):
    if nums[i] != nums[i - 1]:
      nums[k] = nums[i]
      k += 1

  return k  # Unique elements ki count return karta hai