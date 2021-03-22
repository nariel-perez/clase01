###EN ESTE ARCHIVO: EJERCICIOS DEL 2.15 AL 2.18#####


#%% 1 Ejercicio 2.15 : Lista de tuplas
########################### modificado para usar el modulo csv
import csv


'''
def leer_camion(nombre_archivo):
    camion=[]
    f=open('../Data/'+str(nombre_archivo))
    rows=csv.reader(f)
    header=next(rows)
    header
    for row in rows:
        try:
            lote=(row[0],int(row[1]),float(row[2]))
            
            if row[0]=='' or row[1]=='':
                    raise ValueError('valor faltante')
            camion.append(lote)
        except ValueError:
            print(f'Warning:datos faltantes para {row[0]}')
    #print(total)
    return camion   
    f.close()



camion=leer_camion('camion.csv')

print(camion)

#%% 2

###### Ejercicio 2.16

def leer_camion(nombre_archivo):
    camion=[]
    f=open('../Data/'+str(nombre_archivo))
    rows=csv.reader(f)
    header=next(rows)
    header
    for row in rows:
        try:
            lote={'nombre':row[0],'cajones':int(row[1]),
                  'precio':float(row[2])}
            #lote['cajones']=int(row[1])
            #lote['precio']=float(row[2])
            
            if row[0]=='' or row[1]=='':
                    raise ValueError('valor faltante')
            camion.append(lote)
        except ValueError:
            print(f'Warning:datos faltantes para {row[0]}')
    #print(total)
    return camion  
    f.close()



salida=leer_camion('camion.csv')

print(salida)

#%% 3

##### Ejercicio 2.17 Diccionarios como contenedores
def leer_precios(nombre_archivo):
    precios = {} 
    f=open('../Data/'+str(nombre_archivo))

    lines=csv.reader(f)
    for row in lines:
        try:
            precios[row[0]]=float(row[1])
        except:
                continue
    return precios


precios=leer_precios('precios.csv')
'''
#%% 4
#####Ejercicio 2.18 Balances
###lectura del camion###

def leer_camion(nombre_archivo):
    camion=[]
    f=open('../Data/'+str(nombre_archivo))
    rows=csv.reader(f)
    header=next(rows)
    header
    for row in rows:
        try:
            lote={'nombre':row[0],'cajones':int(row[1]),
                  'precio':float(row[2])}
            #lote['cajones']=int(row[1])
            #lote['precio']=float(row[2])
            
            if row[0]=='' or row[1]=='':
                    raise ValueError('valor faltante')
            camion.append(lote)
        except ValueError:
            print(f'Warning:datos faltantes para {row[0]}')
    #print(total)
    return camion  
    f.close()
     

###lectura de los precios finales
def leer_precios(nombre_archivo):
    precios = {} 
    f=open('../Data/'+str(nombre_archivo))

    lines=csv.reader(f)
    for row in lines:
        try:
            precios[row[0]]=float(row[1])
        except:
                continue
    return precios
    f.close()

camion=leer_camion('camion.csv') 
precios=leer_precios('precios.csv')

balance=0.0
for i in camion:
    gasto=i['cajones']*i['precio']
    producto=i['nombre']
    entrada=precios[producto]*i['cajones']
    balance += entrada-gasto
    
print(f'balance final: ${balance:.2f}')
