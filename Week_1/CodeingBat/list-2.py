def count_evens(nums):
  a = [i for i in nums if i % 2 == 0]
  return len(a)

def big_diff(nums):
  return abs(max(nums) - min(nums))

def centered_average(nums):
  nums.remove(max(nums))
  nums.remove(min(nums))
  return sum(nums)/len(nums)

def sum13(nums):
  res = 0
  for i in range(len(nums)):
    if nums[i] != 13:
      res += nums[i]
    else: 
      i+1
  return res

def has22(nums):
  for i in range(len(nums)-1):
    if nums[i] == 2 and nums[i+1] == 2:
      return True
  else:
    return False
      
