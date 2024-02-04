# Variables are dynamically typed i.e type is deternimed at runtime

n = 0
print(n)

n = "abc"
print(n) 

# Multiple assignment
n, m = 0, "abc"
n, m, z = 0.125, "abc", True

#Increment
n = n + 1 #good
n += 1 #good
n++ #bad

# None is null in other languages
n = 4
n = None
print(n)

# If statements don't need parenthesis or curly braces
n = 1
if n > 2:
  n -= 1
elif n ==2:
  n *= 2
else:
  n += 2

# Parenthesis needed if there are multiple statements in the if block
# and = &&
# or = ||

n, m = 1, 2
if((n > 2 and n != m) or n == m):
  n += 1

# While loops are similar 
n = 0
while n < 5:
  print(n)
  n += 1

# Looping form i=0 to i=4
for i in range(5):
  print(i)

for i in range(2, 6):
  print(i)

for i in range(5, 1, -1):
  print(i)

# Division is decimal by default
print(5 / 2)  #2.5

# Double slah rounds down
print(5 // 2) #2

# CAREFUL: most languages round down to 0 by default so negative numbers will round down
print(-3 // 2)  # -2

# A workaround for rounding down is to use the decimal division and then convert to int
print(int(-3 / 2))  # -1

# Modding is similar to most languages
print(10 % 3) # 1

# Except for negative values 
print(-10 % 3)  #2

# To be consistent with other languages modulo
import math
print(math.fmod(-10, 3))  #-1

# More math helper
print(math.floor(3/2)) 
print(math.ceil(3/2))
print(math.sqrt(2))
print(math.pow(2, 3))

# Max / Min Int
float("inf")
float("-inf")

# Python numbers are infinite so they never overflow
print(math.pow(2, 200))

# But still less than infinity
print(math.pow(2, 200) < float("inf"))


# Arrays(called list in python)
arr = [1, 2, 3, 4, 5]
print(arr)

# Can be used as stacks
arr.append(6)
print(arr)

arr.pop()
print(arr)

arr.insert(1, 7)   #inserts 7 at index 1 
print(arr)          # O(n)

# Below is O(1) 
arr[0] = 0
arr[3] = 0  


# Initialise arr of size n(i.e variable size) with default value 1  
n = 5
arr = [1] * n
print(arr)
print(len(arr))


##################################################

# Careful: -1 is not out of bound in python
# it's the last element
arr = [1, 2, 3]
print(arr[-1])

# Indexing -2 is the second last element
print(arr[-2])

###########################################

# Sublist (aka slicing)
arr = [1, 2, 3, 4]
print(arr[1:3])

# Similar to for-loop ranges, last index is non-inclusive
print(arr[0:4])

########################################

#  Unpacking
a, b, c = [1, 2, 3]

# Be careful though
a, b = [1, 2, 3]

########################################

# Loop through arrays
nums = [1, 2, 3]

# Using index
for i in range(len(nums)):
  print(nums[i])

# Without index
for n in nums:
  print(n)

# With index and value
for i, n in enumerate(nums):
  print(i, n)

###############################

# Loop through multiple arrays simultaneously with unpacking
nums1 = [1, 3, 5, 7]
nums2 = [2, 4, 6]

for n1, n2 in zip(nums1, nums2):
  print(n1, n2)  

####################################

# Reverse
nums = [1, 3, 5, 7]
nums1.reverse()

# Reversing specific part
nums[1:4] = nums[3:0:-1]
print(nums)

nums[1:4] = reversed(nums[1:4])

# Extras
reversed_iterator = reversed(nums1[1:4])

for element in reversed_iterator:
  print(element, end=" ")

####################################



# Sorting
arr = [5, 3, 1, 2, 4]
arr.sort()
print(arr)

###################################

arr = ["bob", "aice", "jane", "doe"]
arr.sort()
print(arr)

# Custom sort (by length of string)
arr.sort(key=lambda x:len(x))
print(arr)

####################################

# List comprehension
arr = [i for i in range(5)]
print(arr)
arr = [i * i for i in range(5)]
print(arr)

###################################


# 2-D lists
arr = [[0] * 4 for i in range(4)]
print(arr)

# This won't work
arr = [[0] * 4] * 4  # Each row will be same

########################################

# String are similar to arrays
s = "hello "
print(s[0:2])

# String are immutable so this creates new string

s += "def"    O(n)
print(s) 

######################################

# Valid numeric strings can be converted to int
print(int("123") + int("123"))

# And numbers can be converted to strings
print(str(123) + str(123))

# In rare cases you may need the ASCII vslue of a char
print(ord("a"))
print(ord("b"))

#######################################

# Combine a list of strings (with an empty string delimitor)
strings = ["a", "b", "c"]
print("".join(strings))

# Split a string into a list of strings
s = "a,b,c"
print(s.split(","))

#####################################

# Queue (double ended queue)
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)

queue.pop() 
queue.appendleft(1)
queue.popleft()


#####################################

# Hashset (Accessing and removing element is O(1))
mySet = set()

mySet.add(1)
mySet.add(2)
print(mySet)  #{1, 2}
print(len(mySet))  # 2

print(1 in mySet)   #True

mySet.remove(2)

# list to set
print(set([1,2,3]))

# Set comprehension
mySet = { i for i in range(5)}

####################################


# HashMap (aka dictionary)
myMap = {}
myMap["alice"] = 88
myMap["bob"] = 77

myMap["alice"] = 80
print(myMap["alice"])  #80

myMap.pop("alice")
print("alice" in myMap)

myMap = { "alice" = 90, "bob": 70}

# Dict comprehension

myMap = {i: 2*i for i in range(3)}

# Looping through maps

myMap = { "alice": 90, "bob": 70}
for key in myMap:
  print(key, myMap[key])

for val in myMap.values():
  print(val)

for key, val in myMap.items():
  print(key, val)

####################################

# Tuples are like arrays but immutable

tup = (1,2,3)
print(tup)
print(tup[0])

# Can't modify
tup[0] = 0  #❌

# Can be used as key for hash map/set
myMap = {(1,2): 3} #✅
print(myMap[(1, 2)])

mySet = set()
mySet.add((1, 2))
print((1,2) in mySet)

# lists can't be keys
# myMap[[3,4]] = 5  #❌

####################################

# Heaps (aka priority queues) Useful for finding max and min of set of values
import heapq 

# under the hood arrays

# ----------------------

# MINHEAP
minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)

# Min is always at index 0
print(minHeap[0])  

while len(minHeap):
  print(heapq.heappop(minHeap))

# ----------------------
# MAXHEAP

# No max heaps by default, work around is to use min heap and multiply by -1 when push & pop
maxHeap = []
heapq.heappush(minHeap, -3)  # pushing negative values
heapq.heappush(minHeap, -2)
heapq.heappush(minHeap, -4)

# Max is always at index 0
print(-1 * maxHeap[0])  

while len(maxHeap):
  print(-1 * heapq.heappop(maxHeap))

# ---------------------------

import heapq

# Build heap from initial values
arr = [3, 2, 4, 1, 5]
heapq.heapify(arr)

while arr:
  print(heapq.heappop(arr))

######################################

# Functions

def myFun(n,m):
  return n + m

print(myFun(2,3))

# Nested functions have access to outer variables
def outer(a,b):
  c = "c"
  def inner():
    return a + b + c
  return inner()

print(outer("a", "b"))

# Can modify objects but not reassign unless using nonlocal keyword
def double(arr, val):
  def helper():
    # Modifying array works
    for i, n in enumerate(arr):
      arr[i] *= 2

    # will only modify val in the helper scope
    # val *= 2

    # this will modify val outside helper scope
    nonlocal val
    val *=2

  helper()
  print(arr, val)

nums = [1,2]
val = 2
double(nums, val)

########################################

# Class

class MyClass:
  # Constructor
  def __init__(self, nums):
    #  Create member variables
    self.nums = nums
    self.size = len(nums)

  def getLength(self):
    return self.size

  def getDoubleLength(self):
    return 2 * self.getLength()


########################################

# Happy Coding ❤️🚀








