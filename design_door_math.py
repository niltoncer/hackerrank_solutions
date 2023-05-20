x,y = list(map(int,input().split()))
j=1
for i in range(x):
    if i < x//2 :
      print((".|."*j).center(y,"-"))
      j+=2
    elif i==x//2:
        print("WELCOME".center(y,"-"))
    elif i>x//2 :
      j-=2
      print((".|."*j).center(y,"-"))
