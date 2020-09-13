'''       QUESTION:

Triangular Palindrome :

Your are given a string. You need to form a triangular palindrome using the string. The following are the rules for forming the triangular palindrome:

Increase the number of characters in each line. The first line should have one character (i.e. first character of the string). 
From the second line start printing the characters  from 0th index till index=n-1 where n represents line number and then print the reverse of it. 
Continue to do the same until you print all the characters in the string. Then reduce the characters that you print from length of the string to 1. 
However, you need to increase the length of the string printed in each line. You can look at the testcase for a better understanding of the situation.

Input Format : Single line denoting the string that needs to be made as a triangular palindrome.

Input Constraints : 1 <= length(string) <= 10^4

Output Format : Print the triangular palindrome in the described format.

Sample Input :
Terv

Sample Output :
      T
     TeT
    TereT
   TervreT
  TerrrrreT
 TeeeeeeeeeT
TTTTTTTTTTTTT


















HINTS:

1 - Break the pattern into two smaller triangles. 

2 -    i + j = n - 1

3 -    i = j


'''











































# ANSWER:

a=input()
r=len(a)*2-1
c=r
for i in range(r):
    for j in range(c-1):
        if (i+j)>=(r-1):
            x=min(((r-1)-i),((i+j)-(r-1)))
            print(a[x],end="")
        else:
            print(end=" ")
    for j in range(c):
        if i>=j:
            print(a[min((r-1)-i,(i*2)-(i+j))],end="")
        else:
            print(end=" ")
    print()
