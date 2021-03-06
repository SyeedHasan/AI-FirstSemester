# Additional basic list exercises

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
def remove_adjacent(nums):
    lenNums = len(nums)
    newList = []

    for N in range(0, lenNums):
        try:
            if nums[N+1] == nums[N]:
                pass
            else:
                newList.append(nums[N])

        except IndexError:
            newList.append(nums[-1])

    return newList

# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(listA, listB):

    # Code below,

    countA = 0
    countB = 0
    newList = []

    while listA and listB:
    #if listA and listB:

        if listA[countA] < listB[countB]:
            newList.append(listA[countA]);
            #countA += 1
            listA.remove(listA[countA])

        else:
            newList.append(listB[countB]);
            #countB += 1
            listB.remove(listB[countB])

    newList += listA + listB


    return newList

# Note: the solution above is kind of cute, but unforunately list.pop(0)
# is not constant time with the standard python list implementation, so
# the above is not strictly linear time.
# An alternate approach uses pop(-1) to remove the endmost elements
# from each list, building a solution list which is backwards.
# Then use reversed() to put the result back in the correct order. That
# solution works in linear time, but is more ugly.


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  # if got == expected:
  #   prefix = ' OK '
  # else:
  #   prefix = '  X '

  # print(prefix.ljust(9) + " - Received Output: " + got.ljust(25) + " - Expected Output:" + expected.ljust(10))
  print(got, expected)

# Calls the above functions with interesting inputs.
def main():
  print ('remove_adjacent', end="\n\n")
  test(remove_adjacent([1, 1, 1, 2, 2, 2, 3, 5, 5]), [1, 2, 3, 5])
  test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
  test(remove_adjacent([]), [])
  print()

  print ('linear_merge', end="\n\n")
  test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])
  test(linear_merge([1, 45, 54, 202], [2, 111, 121, 2213]),
       [1, 2, 45, 54, 111, 121, 202, 2213])
  print()


if __name__ == '__main__':
  main()
