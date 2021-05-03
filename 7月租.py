a=int(input("輸入月租類型"))
b=int(input("通話秒數"))
if a == 186:
    if b *0.09  <= 186:
        print(round(b*0.09*0.9))
    else:
        print(round(b*0.09*0.8))
elif a == 386:
    if b *0.08  <= 386:
        print(round(b*0.08*0.8))
    else:
        print(round(b*0.08*0.7))
elif a == 586:
    if b *0.07  <= 586:
        print(round(b*0.07*0.7))
    else:
        print(round(b*0.07*0.6))
elif a == 986:
    if b *0.06 <= 986:
        print(round(b*0.06*0.6))
    else:
        print(round(b*0.07*0.5))
else:
    print("錯誤")