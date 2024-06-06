N=input()
sum=0
for i in range(len(N)):
    if N[i]=='a' or N[i]=='e' or N[i]=='i' or N[i]=='o' or N[i]=='u':
        sum+=1
print(sum)