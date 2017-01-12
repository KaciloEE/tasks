def unique_in_order(iterable):
  ls =[]
  if len(iterable) != 0:
    ls = [iterable[0]]
    for s in iterable[1:]:
      if ls[-1] != s:
        ls.append(s)
  return ls

print (unique_in_order([]))

#['A','B','C','D','A','B']
