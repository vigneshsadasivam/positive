n=int(input("enter n"))
a=[]
for i in range(0,n):
  b=int(input())
  a.append(b)
k=int(input("enter k"))
if(k in a):
  print("yes")
else:
  print("no")
