#Here i follow one algorithm to slove the problem
#algorithm
#step1:-In any magic square,1 is located at position (n/2,n-1)
#step2:-Let's say the position of 1 i.e. (n/2, n-1) is (p, q), then next number which is 2 is located at (p-1, q+1) position. 
       Anytime if the calculated row position becomes -1 then
       make it n-1 and if column position becomes n then make it 0.
#step3:- If the calculated position already contains a number then decrement the column by 2 and increment the row by 1. 
#step4:- If anytime row position becomes -1 and column becomes n, switch it to (0, n-2).

def magic_square(n):
    magicSquare=[]
    for i in  range(n):
        l=[]
        for j in range(n):
            l.append(0)
    for i in range(n):
        for j in range(n):
            print(magicSquare[i][j],end="")
        print()
    i=n//2
    j=n-1
    num=n*n
    count=1
    while(count<=num):
       if(i==-1 and j==n):
        j=n-2
        i=0
        else:
            if(j==n):
                j=0
            if(i<0):
                i=n-1
        if(magicSquare[i][j]!=0):
            j=j-2
            i=i+1
            continue
        else:
        magicSquare[i][j]=count
        count+=1
        i=i-1
        j=j+1
for i in range(n):
    for j in range(n):
        print(magicSquare[i][j],end="")
    print()
    print("The sum of row/column/diagonal is :" +str(n*(n**2)/2))
magic_square(3)
