a=int(input("Entrer le premier entier\t"))
b=int(input("Entrer le second entier\t"))
c=int(input("Entrer le troisième entier\t"))
if a<=b<=c or c<=b<=a:
    print (b)
elif a<=c<=b or b<=c<=a:
    print (b)
else:
    print (a)
