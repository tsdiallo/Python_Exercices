a=int(input("Entrer la valeur a de la combinaison: "))
b=int(input("Entrer la valeur b de la combinaison: "))
print("La combinaison est: ",a, ",",b)
if(a==b):
    print("la combinaison rapporte 10points")
elif(b==a+1 or b==a-1):
          print("La combinaison rapporte 3points")
else:
    print("La combinaison ne rapporte rien")
