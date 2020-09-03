#We start by specify the first three numbers in the sequence
#Then we put it all in a for loop that continues to work until desired length is reached
#The program adds the last three numbers together to form a new number until desireable length is reached
#Finally it prints out the sequence

n = int(input("Enter the length of the sequence: ")) # Do not change this line
n1 = 1
n2 = 2
n3 = 3

for i in range(n):
    if n>=1:
        print(n1)
    n_next=(n1+n2+n3)
    n1=n2
    n2=n3
    n3=n_next