# @sumar
#n1, solicita un numero 
#n2, solicita otro numero
# retur , la suma de los dos numeros

def suma(n1,n2):
    return n1+n2

def restar (n1,n2):
    return n1-n2

def multiplicar(n1,n2):
    return n1*n2

def divicion(n1,n2):
    return n1/n2



def operaciones(nombre,n1,n2):
    print(nombre)
    print(15*"-")
    print("suma :",suma(n1,n2))
    print("resta :",restar(n1,n2))
    print("multiplicar :",multiplicar(n1,n2))
    print("dividir :",divicion(n1,n2))
    print(15*"-")

def nombre(nombre,edad):
    print("nombre",nombre)
    print("edad",edad)
    


operaciones("Beyla",10,5,)
operaciones("angel",10,15,)





