def unlimited_power(x, n):
  if n == 0:
    return 1
  else:
    return -x * unlimited_power(-x, n-1)
print(unlimited_power(6, 13))
