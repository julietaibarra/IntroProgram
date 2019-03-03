
def mostrar(x,y,z):
    if x>y  and x>z:
        return x,"es mayor"
    elif y>x and y>z:
       return y, "es mayor"
    elif z>x and z>y:
        return z,"es mayor"
x=int(input("Ingrese un numero x:"))
y=int(input("Ingrese un numero y:"))
z=int(input("Ingrese un numero z:"))
print(mostrar(x,y,z))
