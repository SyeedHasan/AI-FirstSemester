# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
  # Code below,

  if len(s)>=3:
    if(s[-3:] == 'ing'):
        s += "ly"
    else:
        s += "ing"

  return s
 

# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
  # Code below,
  indexOfNot = s.find("not");
  indexOfBad = s.find("bad");

  if indexOfBad > indexOfNot and indexOfNot!=-1:
    s = s.replace(s[indexOfNot:indexOfBad+3], "good")

  return s


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
    #Code below,
    # lenA = len(a)
    # lenB = len(b)

    # if lenA%2 == 0:
    #     frontA = a[: int(len(a)/2)]
    #     backA = a[int(len(a)/2):]
    # else:
    #     frontA = a[:int(len(a)/2)+1]
    #     backA = a[int(len(a)/2)+1:]

    # if lenB%2 == 0:
    #     frontB = b[: int(len(b)/2)]
    #     backB = b[int(len(b)/2):]
    # else:
    #     frontB = b[:int(len(b)/2)+1]
    #     backB = b[int(len(b)/2)+1:]


    # newString = frontA + frontB + backA + backB

    # return newString

    #Alternate solution
    aHalf = int(len(a)/2)
    if len(a)%2 == 1:
      aHalf+=1

    bHalf = int(len(b)/2)
    if len(b)%2 == 1:
      bHalf+=1

    newString = a[:aHalf]+b[:bHalf]+a[aHalf:]+b[bHalf:]

    return newString


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '

  print(prefix.ljust(9) + " - Received Output: " + got.ljust(25) + " - Expected Output:" + expected.ljust(10))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print ('verbing')
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print ('not_bad')
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print ('front_back')
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()
