'''       QUESTION:

Board Game - Riot Of Pawns :

Fight of Pawns

Chess is a two-player strategy board game played on a checkered board with 64 squares arranged in an 8×8 grid. 
The game is played by millions of people worldwide. 
Pawn might take smaller steps but yet is considered to be one of the most powerful coins. 
Since the pawns performed well in a particular war, they were given a promotion to bishop category. 
A Bishop is possible to move along any diagonal. "With greater power comes greater responsibilities" is a statement from the Spiderman movie, yet a line with great meaning. 
The Pawns weren't that much responsible for the newer power. They started fighting against each other, so if any other pawn was in its path, they will attack each other.

Given a N * N grid, and a value P which specifies the number of pawns and followed by P values which specify the position of those pawns(promoted to bishops).

On our special chessboard, two pawns attack each other if they share the same diagonal. 
This includes pawns that have another pawn located between them, i.e. pawn can attack through pieces.

Find the number of pairs of attacks is possible?

Input Format : The first line of input has two integers - N and K - The grid size and the number of Pawns.
The next P lines of input contain two integers X and Y - the coordinates of each Pawn who were promoted to Bishops.

Input Constraints : 1 ≤ N ≤ 10^4
                    1 ≤ P ≤ MIN( N*N, 10^4 )
                    0 ≤ X, Y ≤ N-1

Output Format : The output contains a single integer - The possible number of pairs of attacks.

Sample Input :
5 4
0 0
0 2
1 1
2 0

Sample Output :
4




















HINTS:

1 - Since the constraints are large, building a grid is not a good idea.

2 - For a grid of size NxN, there are 2*N-1 diagonal elements. And there are 2 types of diagonals.

3 - When there are P pawns in the same diagonal, P*(P-1)/2 attacks are possible.

'''
































# ANSWER:

n, p = map(int, input().split())

diag = [0 for i in range(2*n-1)]
rdiag = [0 for i in range(2*n-1)]

for _ in range(p):
    x, y = map(int, input().split())

    diag[x+y] += 1
    rdiag[x-y+n-1] += 1

ans = 0
for i in range(2*n-1):
    ans += (diag[i] * (diag[i]-1)) // 2
    ans += (rdiag[i] * (rdiag[i]-1)) // 2

print(ans)
