m=int(input("Entrer le montant à régler\t"))
exc=0
if (m%20==0):
    exc=m%20
    print ("Le montant de l'excédent est: ",exc, "euro")
else:
    exc=(20-(m%20))
    print ("Le montant de l'excédent est: ",exc, "euros")
