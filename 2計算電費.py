a=int(input("輸入："))
if 0<a<=120:
    b=a*2.1
    c=a*2.1
if 121<=a<=330:
    b=(a-120)*3.02+120*2.1
    c=(a-120)*2.68+120*2.1
if 331<=a<=500:
    b=(a-330)*4.39+210*3.02+120*2.1
    c=(a-330)*3.61+210*2.68+120*2.1
if 501<=a<=700:
    b=(a-500)*4.97+170*4.39+210*3.02+120*2.1
    c=(a-500)*4.01+170*3.61+210*2.68+120*2.1
if a>701:
    b=(a-700)*5.63+200*4.97+170*4.39+210*3.02+120*2.1
    c=(a-700)*4.50+200*4.01+170*3.61+210*2.68+120*2.1
print("Summer months:",b)
print("Non-Summer months:",c)