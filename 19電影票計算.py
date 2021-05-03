n=int(input("組數為:"))
for i in range(n):
    a,b=map(int,input("第"+str(i+1)+"組:").split())
    c=a*250+b*175
    print("第"+str(i+1)+"組應收費用:"+str(c))