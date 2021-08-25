'''
Caesar cipher is a type of substitution cipher in which 
each letter in the plaintext is replaced by a letter some 
fixed number of positions down the alphabet.

For example, with a left shift of 3, 
'd' would be replaced by 'a'
'e' would be replaced by 'b'
'a' would be replaced by 'x'

input will be 
1. s: a lower-case alphabetic with size below 1e6
2. k: replaced down by k and 1 < k < 100

Examples:

input:
s = "def", k = 3

output:
"abc"

input:
s = "abc", k = 2

output:
"yza"
'''