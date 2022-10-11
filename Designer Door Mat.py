high,n = map(int,input().split())    

high=int((high+1)/2)
mid=int((n-3)/2)
width=mid
a="-"
c=".|."
for i in range(1,high-1):                                #upper part
    if(i==1):
        print((a*mid)+c+(a*mid))
    print((c*i).rjust(width,"-")+c+(c*i).ljust(width,"-"))
print("WELCOME".center(width*2+3,"-"))                     #middle part
i=high-1
while(i>=1):                                               # lower part
    print((c*(i-1)).rjust(width,"-")+c+(c*(i-1)).ljust(width,"-"))
    i-=1