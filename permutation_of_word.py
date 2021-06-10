'''Output Format:

Print the permutations of the string  on separate lines.

Sample Input:

HACK 2
Sample Output

AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH'''

from itertools import permutations
s,n = input().split()
print(*[''.join(i) for i in permutations(sorted(s),int(n))],sep='\n')
