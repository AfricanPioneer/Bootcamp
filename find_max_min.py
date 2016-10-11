def find_max_min(alist):
  max_num = max(alist)  # assigning maximum num to second position
  min_num = min(alist)  # assigning minimum num to first position

  if max_num == min_num:
      return [len(alist)]
  else:
      return [min_num,max_num]