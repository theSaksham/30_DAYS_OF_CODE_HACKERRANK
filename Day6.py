# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for i in range(0,n):
    word = input()
    print(word[::2],word[1::2]) 
