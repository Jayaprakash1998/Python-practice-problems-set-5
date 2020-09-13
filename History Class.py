'''       QUESTION:

History Class :

Abhimanyu was a character of the ancient Indian epic Mahabharata. Abhimanyu was the youngest and 4th son of Arjuna. 
Abhimanyu was the most loved of all sons of the Pandavas.

Abhimanyu is very good at forming chakravyuha with soldiers. 
Chakravyuha is a spiral pattern, ends at its center.

Now you are assigned a task by your history teacher to form the pattern with the number.  
A number n is given, form a pattern of that size such that it reaches the mid if the spiral.

Input Format : Single input N

Input Constraints : 1 <= N <= 500

Output Format : The output contains N lines - The Spiral Pattern.

Sample Input :
5

Sample Output :
1 2 3 4 5 
16 17 18 19 6 
15 24 25 20 7 
14 23 22 21 8 
13 12 11 10 9 



















HINTS:

1 - Approach the Square matrix ring by ring.

2 - At each ring, find a way to traverse the ring. Fill the numbers as in the traversal order.

3 - Start with 1. Traverse the 1st N-1 elements in the 1st row. Then first N-1 elements in the last column. Followed by the last N-1 elements of the last row. 
    Then last N-1 elements of the 1st column. Traverse each ring and fill the numbers.

'''










































# ANSWER:

n = int(input())

ar = [[0 for j in range(n)] for i in range(n)]
num = 1
for l in range(n//2):
    x = n - 2*l - 1

    for j in range(l, l+x):
        ar[l][j] = num
        num += 1

    for i in range(l, l+x):
        ar[i][l+x] = num
        num += 1

    for j in range(l+x, l, -1):
        ar[l+x][j] = num
        num += 1

    for i in range(l+x, l, -1):
        ar[i][l] = num
        num += 1

if(n%2 == 1):
    ar[n//2][n//2] = num

for x in ar:
    print(*x)
