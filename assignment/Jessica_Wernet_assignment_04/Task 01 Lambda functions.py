array_nums = [1, 2, 3, 5, 7, 8, 9, 10]
print("Original arrays:")
print(array_nums)
even_ctr = (list(filter(lambda x: (x%2 == 0) , array_nums)))
print("\nEven numbers: ", even_ctr)