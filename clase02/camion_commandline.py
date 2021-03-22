#%% 1 Ejercicio 2.10

import csv
import sys

def costo_camion(nombre_archivo):
    total=0.0
    f=open(str(nombre_archivo))
    rows=csv.reader(f)
    header=next(rows)
    header
    for row in rows:
        try:
            #rows=csv.reader(f)
            row0=row[0]
            row1=row[1]
            row2=row[2]
            if row1=='' or row2=='':
                    raise ValueError('valor faltante')
            total+=int(row1)*float(row2)
           
        except ValueError:
            print(f'Warning:datos faltantes para {row0}')
    #print(total)
    return total
    
    f.close()
    



if len(sys.argv)==2:
    nombre_archivo=sys.argv[1]
else:
    nombre_archivo='../Data/camion.csv'


costo_total=costo_camion(nombre_archivo)   
print(f'Costo total {costo_total:.2f} ') 
