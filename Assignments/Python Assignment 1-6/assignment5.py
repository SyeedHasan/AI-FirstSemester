import sys
from operator import itemgetter

"""
Wordcount exercise
Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.
"""

def printWords(wordDict):
  print("Display Mode: Word -- Count".rjust(35))

  sortedDict = sorted(wordDict.items(), key=itemgetter(0))
  # Returns a list of tuples (key, value) pair

  # Reconverted to a dict for ease in printing
  sortedDict = dict(sortedDict)

  totalWordCount = 0

  for key,value in sortedDict.items():
    totalWordCount += value
    print(str(key).rjust(20) + " -- " + str(value))

  print("Total Word Count = " + str(totalWordCount))

"""
2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

def printTop(wordDict):
  print("Display Mode: Word -- Count".rjust(35))

  sortedDict = sorted(wordDict.items(), key=itemgetter(1), reverse=True)
  # Returns a list of tuples (key, value) pair

  # Reconverted to a dict for ease in printing
  sortedDict = dict(sortedDict)

  totalCount = 0

  for key,value in sortedDict.items():
    if totalCount != 20:
      print(str(key).rjust(20) + " -- " + str(value))
      totalCount += 1
    else:
      break


"""
#File reader

"""

def fileReader(userfile):
  userDict = {}
  with open(userfile) as fileObject:
    for line in fileObject:
      wordList = line.split(" ")
      count = 0
      for word in wordList:
        word = word.lower().rstrip()

        if not word.isalpha():
          continue

        if not word in userDict:
          userDict[word] = 1
        else:
          userDict[word] += 1

    return userDict

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print ('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]

  returnedDict = fileReader(filename)

  if option == '--count':
    printWords(returnedDict)
  elif option == '--topcount':
    printTop(returnedDict)
  else:
    print ('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
