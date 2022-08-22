'''1.You are given a sentence, and want to shift each letter by 2 in alphabet to create a secret code.
The sentence you want to encode is "the lazy dog jumped over the quick brown fox."
and the
output should be "vjg ncba fqi lworgf qxgt vjg swkem dtqyp hqz."

I/P-"The lazy dog jumped over the quick brown fox."

O/P-"vjg ncba fqi lworgf qxgt vjg swkem dtqyp hqz." '''

##import string
##n1 = {}
##n2 ={}
##
##for i,letter in enumerate(string.ascii_lowercase):
##    n1[i] = letter
##    n2[letter] = i
##
##s2 = ' '
##for letter in 'the lazy dog jumped over the quick brown fox':
##    if letter in n2:
##        current_letter_number = n2[letter] + 2
##    
##    if current_letter_number == 26:
##            current_letter_number = 0
##    elif current_letter_number == 27:
##            current_letter_number = 1
##    s2+= n1[current_letter_number]
##else:
##    s2+=letter
##
##print(s2)

