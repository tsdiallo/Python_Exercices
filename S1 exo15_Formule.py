x=int(input("Enter une valeur entière\t"))
gauche=1+x+(x**2)+(x**3)
droite=(((x**4)-1))//(x-1)
a=(gauche==droite)
print (a)
