# Basic list exercises

from operator import itemgetter
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# It's ok if you do not complete all the functions, and there
# are some additional functions to try in assignment4_list.py.

# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.
def match_ends(words):
  # Code below,

  count = 0

  for word in words:
    if len(word)>=2:
      if word[0:1] == word[-1:]:
        count += 1

  count = str(count)

  return count


# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
def front_x(words):
  # Code below,
  XList = []

  words.sort()

  for word in words:
    if word[0:1] == "x":
      XList.append(word)

  for word in XList:
    if word in words:
      words.remove(word)

  XList.sort()

  XList += words

  print("Received Output: " , XList)




# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.
def sort_last(tuples):
  # Code below

  tuples.sort(key=itemgetter(-1))

  print(tuples)


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '

  print(prefix.ljust(9) + " - Received Output: " + got.ljust(25) + " - Expected Output:" + expected.ljust(10))


# Calls the above functions with interesting inputs.
def main():

  print ('match_ends')
  test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), "3")
  test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), "2")
  test(match_ends(['aaa', 'be', 'abc', 'hello']), "1")

  print ('front_x')
  print()
  #Removed test for these,
  front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
  print("Expected Output: " , ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
  print()
  front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
  print("Expected Output: " , ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
  print()
  front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
  print("Expected Output: " , ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])
  print()
       
  print ('sort_last')
  sort_last([(1, 3), (3, 2), (2, 1)])
  print("Expected Output : " , [(2, 1), (3, 2), (1, 3)])
  sort_last([(2, 3), (1, 2), (3, 1)]),
  print("Expected Output : " ,[(3, 1), (1, 2), (2, 3)])
  sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
  print("Expected Output : " ,[(2, 2), (1, 3), (3, 4, 5), (1, 7)])


if __name__ == '__main__':
  main()
