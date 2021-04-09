from math import sqrt, pow
def saisie(): #definition de la fonction saisie
    a=int(input("A="))
    b=int(input("B="))
    c=int(input("C="))
    return a, b, c
def delta(l, m, n): #definition de la fonction delta
    return m^2-4*l*n

a, b, c=saisie()
d=delta(a, b, c)
if d==0:
      print("S=", -b//(2*a))
elif d<0:
      print("pas de solutions.")
else:
      print("S1=", (-b-(sqrt(d)))/(2*a), "\n", "S2=",(-b+(sqrt(d)))/(2*a))
