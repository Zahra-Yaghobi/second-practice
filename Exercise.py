# Programmer : Zahra Yaghubi

# a=1
# b=1
# n= int(input("Enter numner : "))
# print(a)
# print(b)
# i=2

# while(i<n):
#     c=a+b
#     print(c)
#     a=b
#     b=c
#     i=i+1
    
sum=0
max =0
min=0
score =[]
n= int(input("enter number of student :"))
for i in range(n):
    score.append(float(input()))
    sum+=score[i]

avg=sum/n
print("avg is : " ,avg )

min =score[0]
max =score[0]
for j in range(n):
    if(score[j] >max):
        max =score[j]
    if(score[j] <min):
        min =score[j]
 
print(" \nMinimum is : " ,  min)
print(" \nMaximum is : " , max )
