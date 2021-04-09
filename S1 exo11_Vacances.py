j=int(input("Entrez le jour:\t"))  
m=int(input("Entrez le mois:\t"))
      
enVacances=(j>8 and m==7 )or (m==8) or (j<3 and m==9)
print("j = ",j," et m = ",m," ->", enVacances)
