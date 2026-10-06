

compra = float(input( "Monto de la compra: "))

descuento = 0
if compra > 30000:
    descuento = compra * 0.05
elif compra > 60000:
    descuento = compra * 0.10
    print( "Descuento:", descuento)
elif compra > 100000:
    descuento = compra * 0.15

total = compra - descuento

print( "Descuento:", descuento)
print( "Total:", total)