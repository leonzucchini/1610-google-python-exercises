# Solution for Google Python Course Day 2 pt 1 - Regular Expressions
# LZ161015

import re
import sys
import os.path
import inspect


def main():
  thisFilePath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) # script directory
  print os.path.abspath(os.path.join(thisFilePath, os.pardir))
# # Import files
# def readText(filename):
# 	f = open(filename, "rU")
# 	text = f.read()
# 	return text

# print readText('baby1990.html')

if __name__ == '__main__':
  main()