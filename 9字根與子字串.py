s1=list(input("輸入"))
s1=set(s1)
s2=list(input("輸入"))
s2=set(s2)
if s1.intersection(s2) == s1:
    print(True)
else:
    print(False)
    
