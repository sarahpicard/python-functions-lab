# challenge 1 - write a function that accepts a single integer, and returns the sum of the integers from 1 to n
def sum_to(n):
  total = 0
  for n in range(1, n + 1):
    total += n
  return total

# print(sum_to(12))




# challenge 2 - write a function that takes a list of numbers as an argument and returns the largest number in that list
def largest(ns):
  ns.sort()
  return ns[-1]

# print(largest([1, 2, 3, 4, 0]))





# challenge 3 - write a function that takes two string arguments as input and counts the number of occurrences of the second string inside the first string
def occurrences(str1, str2):
  return str1.count(str2)

# print(occurrences('fleep floop', 'e'))





# challenge 4 - write a function that takes an arbitrary number of numbers, multiplies them all together, and returns the product. 

def product(*args):
  product = 1
  for arg in args:
    product *= arg
  return product

# print(product(-1, 4))