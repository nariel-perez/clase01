####CLASE 02####

##Ejercicio 2.2: Lectura de un archivo de datos####


'''
total=0.0
f=open('../Data/camion.csv' ,'r')
header=next(f)
for line in f:
    rows=line.split(',')
    row1=rows[1]
    row2=rows[2]
    total+=int(row1)*float(row2)
print(f'Costo total {total} ')    
f.close()
'''

###Ejercicio 2.6: Transformar un script en una funcion
'''
def costo_camion(nombre_archivo):
    total=0.0
    f=open('../Data/'+str(nombre_archivo),'r')
    header=next(f)
    for line in f:
        rows=line.split(',')
        row1=rows[1]
        row2=rows[2]
        total+=int(row1)*float(row2)
    print(f'Costo total {total} ')    
    f.close()

costo_camion('camion.csv')
#costo_camion('missing.csv')
''' 

####Ejercicio 2.8: Administracion de errores

def costo_camion(nombre_archivo):
    total=0.0
    f=open('../Data/'+str(nombre_archivo),'r')
    header=next(f)
    for line in f:
        try:
            rows=line.split(',')
            row0=rows[0]
            row1=rows[1]
            row2=rows[2]
            if row1=='' or row2=='':
                raise ValueError('dato faltante')

            total+=int(row1)*float(row2)
        except ValueError:
            print(f'Warning:datos faltantes para {row0}')
            
    print(f'Costo total {total:.2f}')
    f.close()


archivos=['missing.csv', 'camion.csv']

for archivo in archivos:
        costo_camion(archivo)
        

