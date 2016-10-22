#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""



def extract_names(filename):
  
  # Read text from file
  f = open(filename, 'rU')
  text = f.read()

  names = []

  # Get year
  year_match = re.search('Popularity\sin\s(\d\d\d\d)', text)
  if not year_match:
    sys.stderr.write('Couldn\'t find a year!')
    sys.exit(1)
  year = year_match.group(1)
  names.append(year)

  # Get rank of m/f names as tuples (number, boysname, girlsname)
  tuples = re.findall('<td>(\d*)</td><td>(\w*)</td><td>(\w*)</td>', text)
  # print tuples

  names_to_rank = {}

  for rank_tuple in tuples:
    (rank, boysname, girlsname) = rank_tuple
    
    if boysname not in names_to_rank.keys():
      names_to_rank[boysname] = rank
    if girlsname not in names_to_rank.keys():
          names_to_rank[girlsname] = rank

  sorted_keys = sorted(names_to_rank.keys())

  for name in sorted_keys:
    names.append(name + ' ' + names_to_rank[name])

  return names


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  for filename in args:
    names = extract_names(filename)
    text = '\n'.join(names)

    if summary:
        # print filename + '.summary' + '.py'
        outf = open(filename + '.summary', 'w')
        outf.write(text + '\n')
        outf.close()
    else: 
      print text

  
if __name__ == '__main__':
  main()
