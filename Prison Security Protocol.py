'''       QUESTION:

Prison Security Protocol :

There is a highly secure prison that holds the most dangerous criminals in the world. On 2nd November 2019, 
the prison officials received a warning that there was an attack planned on the prison to free the criminals. 
So, the prison officials planned a quick evacuation plan. They planned to shift all the criminals in the prison to a different place.

A military level armored vehicle is waiting at the prison gate, they want to load all the prisoners inside the vehicle so they can be transferred to a secure location. 
The prison has a certain number of cells and each cell has a certain number of people and no cells are empty. 
As a safety method, the prison officials would like to group two cells together at one time, so prisoners from two cells will be moved to a dormitory. 
Once you narrow the prisoners to two dormitories, you can then combine them to send them into the armored vehicle. 
Shifting one prisoner from one cell to another will take one minute.

For example, let’s say there are three cells A, B and C. Prisoner from any of the two cells are moved to a dormitory, 
let’s say we are combining cells A and B to form AB, now we are left with two blocks of prisoners, now we can add them to the vehicle, 
so what will be the minimum time taken in total to load all the prisoners into the vehicle?

Input Format : 
  The first line of input has one integer input N, where N is the number of cells in the prison.
  The second line of input has N spaced integers specifying the number of prisoners in each cell and no cell is empty.

Input Constraints : 2<=N<=10^9
                    1<=a[i]<=10^9
                    N - Number of cells
                    a[i] - prisoner count in i'th cell

Output Format : Minimum possible integer

Sample Input :
8
1 2 3 4 5 6 7 8

Sample Output :
119





















HINTS:

1 - Sometimes it's better to have things in order.

2 - Sort in ascending order.

3 - Prefix sum.

'''


































# ANSWER:

n = int(input())
l = list(map(int,input().split(' ')))
l.sort()
s = (n-1)*l[0]
for i in range(1,n):
    s+= ((n-i)*l[i])
print(s)
