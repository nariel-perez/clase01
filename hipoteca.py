# hipoteca.py
# Archivo de ejemplo
# Ejercicio de hipoteca


###ejercicio 1.7: La hipoteca de David ###
''''
saldo=500000
tasa=0.05
pago_mensual=2684.11
total_pagado=0.0
meses=0
while saldo>0:
   
    saldo=saldo*(1+tasa/12)-pago_mensual
    total_pagado+=pago_mensual

print('total pagado: ',round(total_pagado,2))

'''

####ejercicio 1.8: Adelantos #####

'''
saldo=500000
tasa=0.05
pago_mensual=2684.11
total_pagado=0.0
meses=0
pago_extra=1000
while saldo>0:
    meses+=1
    if meses <=12:
        saldo=saldo*(1+tasa/12)-pago_mensual-pago_extra
        total_pagado+=pago_mensual+pago_extra
    else:
        saldo=saldo*(1+tasa/12)-pago_mensual
        total_pagado+=pago_mensual
    


print('total pagado: ',round(total_pagado,2))
print(meses)
'''

###ejercicio 1.9: Calculadora de Adelantos ####
'''
saldo=500000
tasa=0.05
pago_mensual=2684.11
total_pagado=0.0
meses=0
pago_extra=1000
pago_extra_mes_comienzo=61
pago_extra_mes_fin=108

while saldo>0:
    meses+=1
    if meses >=pago_extra_mes_comienzo and meses<=pago_extra_mes_fin :
        saldo=saldo*(1+tasa/12)-pago_mensual-pago_extra
        total_pagado+=pago_mensual+pago_extra
    else:
        saldo=saldo*(1+tasa/12)-pago_mensual
        total_pagado+=pago_mensual
    


print('total pagado: ',round(total_pagado,2))
print(meses)
'''

###ejercicio 1.10: Tablas ###
'''
saldo=500000
tasa=0.05
pago_mensual=2684.11
total_pagado=0.0
meses=0
pago_extra=1000
pago_extra_mes_comienzo=61
pago_extra_mes_fin=108

while saldo>0:
    meses+=1
    if meses >=pago_extra_mes_comienzo and meses<=pago_extra_mes_fin :
        saldo=saldo*(1+tasa/12)-pago_mensual-pago_extra
        total_pagado+=pago_mensual+pago_extra
    else:
        saldo=saldo*(1+tasa/12)-pago_mensual
        total_pagado+=pago_mensual
    
    print(meses,round(total_pagado,2), round(saldo,2))

print('total pagado: ', round(total_pagado,2))
print('meses: ', meses)
'''
###ejercicio 1.11: BONUS###
##Del ejercicio anterior se sabe que el ultimo mes es el 310, entonces
# es necesario ajustar en ese mes....
saldo=500000
tasa=0.05
pago_mensual=2684.11
total_pagado=0.0
meses=0
pago_extra=1000
pago_extra_mes_comienzo=61
pago_extra_mes_fin=108

while saldo>0:
    meses+=1
    if meses >=pago_extra_mes_comienzo and meses<=pago_extra_mes_fin :
        saldo=saldo*(1+tasa/12)-pago_mensual-pago_extra
        total_pagado+=pago_mensual+pago_extra
    elif meses==310:
        pago_mensual=saldo*(1+tasa/12)
        saldo=saldo*(1+tasa/12)-pago_mensual
        total_pagado+=pago_mensual
    else:
        saldo=saldo*(1+tasa/12)-pago_mensual
        total_pagado+=pago_mensual

    
    print(meses,round(total_pagado,2), round(saldo,2))

print('total pagado: ', round(total_pagado,2))
print('meses: ', meses)

