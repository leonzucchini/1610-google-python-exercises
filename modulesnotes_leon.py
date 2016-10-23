# Google QuickPy Course Module integration 
# Notes Leon
# 161023

import sys

import os
# os.listdir() # return paths in directory as list of strings
# os.path.join(dir, filename) # joint together components to a path
# os.path.abspath(path) # absolute path for a path
# os.path.exists()
# os.mkdir()

import shutil
# shutil.copy(src, dest) # copy path from one place to another

import commands
# commands.getstatusoutput()

def List(dir):
  cmd = 'ls -l ' + dir
  (status, output) = commands.getstatusoutput(cmd)
  sys.stderr.write('there was an error' + output)
  return
  if status:
    sys.exit(1)
  print output

  # # example for os.path
  # filenames = os.listdir(dir)
  # for filename in filenames:
  #   path = os.path.join(dir, filename)
  #   print path
  #   os.path.abspath(path)


# Define a main() function that prints a little greeting.
def main():
  List(sys.argv[1])

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
