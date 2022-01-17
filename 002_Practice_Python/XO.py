'''
Check to see if a string has the 
same amount of 'x's and 'o's. The 
method must return a boolean and 
be case insensitive. The string 
can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is 
present should return true

XO("zzoo") => false
'''


import os

def xo(s):
    
    if s.lower().count('x') == s.lower().count('o') or \
        (s.lower().count('x') == 0 and s.lower().count('o') == 0):
        return True
    else:
        return False

s1 = "ooxx"
s2 = "xooxx" 
s3 = "ooxXm"
s4 = "zpzpzpp"
s5 = "zzoo"
print(xo(s1), xo(s2), xo(s3), xo(s4), xo(s5), sep='\n')