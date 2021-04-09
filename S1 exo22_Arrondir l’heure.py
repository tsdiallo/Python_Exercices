#1
n=int(input("Entrer un entier positif ou nul: "))
N=n%5
if (N==0):
    print("Le multiple de 5 le plus proche de",n," est ",n)
elif (N<=4):
    print("Le multiple de 5 le plus proche de",n," est ",n-N)
else:
    print("Le multiple de 5 le plus proche de",n," est ",n+N)


#2
h=int(input("Entrer l'heure comprise entre 0 et 24: h="))
m=int(input("Entrer les minutes comprises entre 0 et 60: m="))
print("l'heure est : ",h,"h",m,"m")
if (m<=2):
    print("L'heure arrondie est ",h,"h 00m")
elif (3<=m<=7):
    print("L'heure arrondie est ",h,"h 05m")
else:
    print("L'heure arrondie est ",h+1,"h 00m")
