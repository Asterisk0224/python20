a=int(input("請輸入階層值M:"))
b=1
c=1
while(c<=a):
    b+=1
    c*=b
print("超過M為",a,"最小階層N值為:",b)