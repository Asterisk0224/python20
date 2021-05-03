mon=int(input("月:"))
day=int(input("日:"))
s=(mon*2+day)%3
if s==0:
    print("普通")
elif s==1:
    print("吉")
elif s==2:
    print("大吉")