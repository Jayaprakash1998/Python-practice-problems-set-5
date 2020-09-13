'''       QUESTION:

Birthday Link :

Victor threw a party on his birthday. It 24 hour long party. Entire party was recorded in a video camera, and he uploaded the video to his google drive. 
He even encrypted the file and saved the file and stored the link as birthday link.
After a few years, he wanted to retrieve the video from the birthday link, but he did happen to forget the password.

1 4 5 16 17 20 21 is a number series, Victor remembered a number N, and the Nth term in the series will be the password for the file. 
So help Victor unlock the birthday link.

Input Format : One single integer input N, where N is the number which Victor remembers

Input Constraints : 1<=N<=10^9

Output Format : One single integer denoting the password for unlocking the birthday video file

Sample Input :
1

Sample Output :
1



















HINTS:

1 - Think like a machine.

2 - Binary.

3 - 4 power Cycle.

'''

















































# ANSWER:

n = int(input())
s = 0
k = 0
while(n):
    if(n&1):
        s+=(1<<k)
    k+=2
    n = n>>1
print(s)
