'''
M2
a = 100
sanoq = 0
son = int(input("Son kiriting: "))
sanoq+=1
if son>=80:
    print("bahoingiz alo")
elif son>=60 and son<=80:
    print("Bahoyingiz yaxshi")
elif son>=40 and son<=60:
    print("Bahoyingiz qoniqrli")
elif son>=0 and son<=40:
    print("Bahoyingiz qoniqrsiz")
else:
    print("Bunday baho yo'q")
print(sanoq)
'''
#----------------------------------------------------------
'''
#M3
a = ord(input("son kirit: "))
if a > 48 and a < 57:
    print("son")
else:
    print("belgi ")
'''
#----------------------------------------------------------
'''
#M4
alfabit = 'q,w,e,r,t,y,u,i,o,p,a,s,d,f,g,h,j,k,l,z,x,c,v,b,n,m'
harf = input("son harf kirit: ")
if harf.lower() in alfabit:
    print("harf")
elif harf not in alfabit:
    print("harf emas")
'''
#----------------------------------------------------------
'''
#M5
son = int(float(input("Son kiriting: ")))
natija = 0
kiritilgan = son

while son > 0:
    a = son % 10
    natija = natija + a
    son = int(son/10)
print(kiritilgan, "sonlari yig'indisi", "bu", natija)
'''
#----------------------------------------------------------
'''
M6 va M7
son = (input("son kirit: "))
print(son[::-1])
'''
