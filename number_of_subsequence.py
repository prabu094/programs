# Python 3 program to count
# subsequences of the form
# a ^ i b ^ j c ^ k

# Returns count of subsequences
# of the form a ^ i b ^ j c ^ k

'''Input  : abbc
Output : 3
Subsequences are abc, abc and abbc

Input  : abcabc
Output : 7
Subsequences are abc, abc, abbc, aabc
abcc, abc and abc
Input  : abbc
Output : 3
Subsequences are abc, abc and abbc

Input  : abcabc
Output : 7
Subsequences are abc, abc, abbc, aabc
abcc, abc and abc'''

def countSubsequences(s):
	aCount = 0
	bCount = 0
	cCount = 0

	# Traverse all characters
	# of given string
	for i in range(len(s)):
	
		# If current character is 'a',
		# then there are following
		# possibilities :
		# a) Current character begins
		# a new subsequence.
		# b) Current character is part
		# of aCount subsequences.
		# c) Current character is not
		# part of aCount subsequences.
		if (s[i] == 'a'):
			aCount = (1 + 2 * aCount)

		elif (s[i] == 'b'):
			bCount = (aCount + 2 * bCount)

		elif (s[i] == 'c'):
			cCount = (bCount + 2 * cCount)

	return cCount

# Driver code
if __name__ == "__main__":
	s = input()
	print(countSubsequences(s))

