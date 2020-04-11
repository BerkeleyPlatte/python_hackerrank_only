# Lilah has a string of lowercase English letters that she repeated infinitely many 
# times.  Given an integer, n, find and print the number of letter a's in the first 
# n letters of Lilah's infinite string.

# Complete the repeatedString function in the editor below. It should return an integer 
# representing the number of occurrences of a in the prefix of length n in the 
# infinitely repeating string.

import math

# Complete the repeatedString function below.
def repeatedString(s, n):
    count = 0
    for each in s:
        if each == 'a':
            count += 1
    remainder = count * math.floor((n / len(s)))
    for each in s[:n % len(s)]:
        if each == 'a':
            remainder += 1
    return remainder

print(repeatedString('aba', 10))