def running_total(deposits):
  i = 0
  for i in range(len(deposits)):
    if i == 0:
      continue
    deposits[i] = deposits[i] + deposits[i-1]
    
  return deposits
