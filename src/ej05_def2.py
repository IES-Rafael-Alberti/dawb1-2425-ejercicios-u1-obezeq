#!/usr/bin/env python3

def calculador(importe: float, iva: float):
    if importe >= 0:

        if iva >= 0 and iva <= 100:
            porcentaje = f"{21:.2f}"
            iva = 1.21
        else:
            porcentaje = f"{iva:.2f}"
            iva = 1 + iva / 100

        total = round((importe * iva), 2)
        total = f"{total:.2f}"
        print(f"El precio final del artículo con IVA ({porcentaje}) es {total}€.")
    else:
        print(f"El importe debe ser mayor o igual a 0")