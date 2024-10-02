#!/usr/bin/env python3

def calcula_precio(importe: float, iva: float):
    if importe >= 0:

        if iva >= 0 and iva <= 100:
            porcentaje = f"{21:.2f}"
            iva = 1.21
        else:
            porcentaje = f"{iva:.2f}"
            iva = 1 + iva / 100

        total = round((importe * iva), 2)
        total = f"{total:.2f}"
        return f"El precio final del artículo con IVA ({porcentaje}) es {total}€."
    
    # Mostrar error en caso que el importe sea menor a 0
    else:
        return "El importe debe ser mayor o igual a 0"
    
def main():
    calcula_precio(10, 21)

if __name__ == '__main__':
    main()