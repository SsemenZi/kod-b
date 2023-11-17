def recursiv_max(lst):
  if len(lst) == 1:
    return lst[0]
  max_in_list = recursiv_max(lst[1:])
  if lst[0] > max_in_list:
    return lst[0]
  return max_in_list
print(recursiv_max([1, 34, 56,76, 9]))