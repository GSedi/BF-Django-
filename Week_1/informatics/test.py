def array_front9(nums):
  if len(nums) < 4:
    return False
  
  for i in range(3):
    if nums[i] == 9:
      return True
  else:
    return False

print(range(20))