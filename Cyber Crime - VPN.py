'''       QUESTION:

Cyber Crime - VPN :

Certain websites are banned by certain countries, but just because they have banned it, it cannot stop the people from using it by using a Virtual Private Network (VPN). 
But the government has started tracking down people who are using illegal websites. 
So the hackers go a step ahead and use VPN and create a pseudo location every second, and they map the data through different servers, 
so it is not easy to trace back to the origin. There are N servers available, and each server will preset data transfer  point. 
Always, the data will be transmitted from the current server to the data transfer point server which is also present in this N servers.

Initially the data is transmitted and it starts bombarding around the servers, and once all the data come to the same arrangement as beginning, 
the pseudo location algorithm will begin functioning. So the cyber crime has very less time to pin down the hackers Each data transfer takes one second, 
and all the servers transmit data at the same time and also receive a data at the same time. 
Help the Cyber Crime to track down the hackers.

Input Format : The first line of input has one single integer input N, 
               where N is the number of servers and the next line of input has N spaced integers which specify the data transfer point of the corresponding server

Input Constraints : 1<=N<=25

Output Format : The time in seconds which the cops have to trace down the hackers

Sample Input :
6
2 5 4 1 6 3

Sample Output :
6

















HINTS:

1 - Find the pattern the swapping follows.

2 - Keep a note of numbers that you have crossed by.

3 - Least common multiple.

'''













































# ANSWER:

from math import gcd as g
n=int(input())
l=list(map(int,input().split()))
m=[]
for i in range(len(l)):
    k=l[i]
    c=0
    while(l[l[i]-1]!=k):
        i=l[i]-1
        c+=1
    m.append(c+1)
k=m[0]
for i in m[1:]:
    k=k*i//g(k,i)
print(k)
