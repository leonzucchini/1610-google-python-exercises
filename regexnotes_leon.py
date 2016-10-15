# Google python class day 2 pt 1 - Regular Expressions

import re
match = re.search('iig', 'called piiig')
#print match.group()

match = re.search('igs', 'called piiig') # match returns none if no match
print match

## Special caracters for re
# . (dot) any character
# \ escape character
# r'' raw string = ignore backslashes
# \w word character (alphabet, number, not punctuation except underbar)
# \d digit
# \s whitespace
# \S non-whitespace
# + one or more
# * zero or more


def Find(pat, text):
	match(pat, text)
	if match: print match.group
	else: print 'not found'

Find(r':\w+', 'blah balh:kitten blah blah')
# matches to the whitespace (word characters)

Find(r':\w+', 'blah balh:kitten&&a123 blah blah')
# matches word characters

Find(r':\S+', 'blah balh:kitten123&a=2351 blah blah')
# matches non-whitespace characters

Find(r'[\w.]+@[\w+.]+', 'blah nick.p@gmail.com yatta @ ')
# sets of characters to look for

Find(r'\w[\w.]*@[\w+.]+', 'blah nick.p@gmail.com yatta @ ')
# sets of characters to look for

m = re.search(r'([\w.]+)@([\w+.]+)', 'blah .nick.p@gmail.com yatta @ ')
# groups of characters that can be addressed as m.group(1)
m.group(2)

re.findall(r'[\w.]+@[\w+.]+', 'blah nick.p@gmail.com yatta foo@bar')
# findall

re.findall(r'([\w.]+)@([\w+.]+)', 'blah nick.p@gmail.com yatta foo@bar')

# additional arguments for re
# DOTALL matches across lines
# IGNORECASE ignores case of lines

# f = open(filename, "w")
# f.write(text)
# open a file for writing


