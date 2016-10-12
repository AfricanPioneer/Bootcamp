def find_missing(list_a, list_b):
  if len(list_a) == 0 and len(list_b) == 0:
    return 0
  elif len(list_a) == len(list_b):
    for num in list_a:
      if num in list_b:
        return 0
  else:
    if len(list_a) < len(list_b):
      for num in list_b:
        if num not in list_a:
          return num

