def first_last6(nums):
  return nums[0] == 6 or nums[len(nums)-1] == 6

def same_first_last(nums):
  return len(nums) >= 1 and (nums[0] == nums[len(nums)-1])

def make_pi():
  return [3, 1, 4]

def common_end(a, b):
  return a[0] == b[0] or a[len(a)-1] == b[len(b)-1]

def sum3(nums):
  return sum(nums)

def rotate_left3(nums):
  nums.append(nums[0])
  nums.remove(nums[0])
  return nums

def reverse3(nums):
  nums.reverse()
  return nums

def max_end3(nums):
  if nums[0] >= nums[2]:
    max = nums[0]
  if nums[0] <= nums[2]:
    max = nums[2]
  res = [max] * 3
  return res
  
def sum2(nums):
  if len(nums) == 0:
    return 0
  elif len(nums) < 2:
    return sum(nums)
  else:
    return sum(nums[:2])

def middle_way(a, b):
  res = [a[1], b[1]]
  return res

def make_ends(nums):
  if len(nums) == 1:
    return nums*2
  else:
    res = [nums[0], nums[len(nums)-1]]
    return res

def has23(nums):
  return 2 in nums or 3 in nums
