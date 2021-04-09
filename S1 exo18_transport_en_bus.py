recommencer=1
while(recommencer==1):
    p=int(input("entrez le nbr de passagers par bus\n"))
    n=int(input("nombre de passagers à transporter\n"))

    if (p = n):
        ndb=1
        print ("il faudra",ndb,"bus pour transporter",n,"passagers.")
    elif (n>p and n%p==0):
        ndb=n/p
        print ("il faudra",ndb,"bus pour transporter",n,"passagers.")
    elif ( n>p and n%p!=0):
        ndb=(n//p)+1
        print ("il faudra",ndb,"bus pour transporter",n,"passagers")
    recommencer=int(input("Voulez-vou recommencer?\n0.non\n1.oui\n"))
