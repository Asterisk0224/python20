mon,day=input("輸入月及日為:").split()
mon=int(mon)
day=int(day)
if mon==1 :
    if 21<=day<=31:
        print("星座為Aquarius")
    elif 1<=day<=20:
        print("星座為Capricorn")
if mon==2:
    if 1<=day<=18:
        print("星座為Aquarius")
    elif 19<=day<=28:
        print("星座為Pisces")
if mon==3:
    if 1<=day<=20:
        print("星座為Aquarius")
    elif 21<=day<=31:
        print("星座為Aries")
if mon==4:
    if 1<=day<=20:
        print("星座為Aries")
    elif 21<=day<=30:
        print("星座為Taurus")
if mon==5:
    if 1<=day<=21:
        print("星座為Taurus")
    elif 22<=day<=31:
        print("星座為Gemini")
if mon==6:
    if 1<=day<=21:
        print("星座為Gemini")
    elif 22<=day<=30:
        print("星座為Cancer")
if mon==7:
    if 1<=day<=22:
        print("星座為Cancer")
    elif 23<=day<=31:
        print("星座為Leo")
if mon==8:
    if 1<=day<=23:
        print("星座為Leo")
    elif 24<=day<=31:
        print("星座為Virgo")
if mon==9:
    if 1<=day<=23:
        print("星座為Virgo")
    elif 24<=day<=30:
        print("星座為Libra")
if mon==10:
    if 1<=day<=23:
        print("星座為Libra")
    elif 24<=day<=31:
        print("星座為Scorpio")
if mon==11:
    if 1<=day<=22:
        print("星座為Scorpio")
    elif 23<=day<=30:
        print("星座為Sagittarius")
if mon==12:
    if 1<=day<=21:
        print("星座為Sagittarius")
    elif 22<=day<=31:
        print("星座為Capricorn")
    
        