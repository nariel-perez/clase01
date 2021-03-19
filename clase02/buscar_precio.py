
def buscar_precio(fruta):
    
    f=open('../Data/precios.csv', 'rt')
    for line in f:
        a=line.split(',')
        if fruta in a[0]:
            precio=float(a[1])
            break
        else:
            precio=0.0
        
    f.close()
    return precio
    



fruta=str(input('ingresar nombre de la fruta: '))

dato=buscar_precio(fruta)

if dato==0.0:
    print(f'La fruta {fruta} no se encuentra en la lista')
else:
    print(f'el valor de {fruta} es: ${dato}')
