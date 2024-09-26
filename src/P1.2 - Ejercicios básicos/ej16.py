#!/usr/bin/env python3

pan = 3.49
descuento = 0.6

try:
    barras_no_dia = int(input("[+] Cuantas barras que no son del dia has vendido? "))
    
    precio_pan = round((pan * barras_no_dia), 2)
    precio_pan_descontado = round((precio_pan * (1 - descuento)), 2)
    descuento_ahorrado = round((precio_pan - precio_pan_descontado), 2)

    print(f"- El precio habitual de una barra vendida del día es: {pan}€")
    print(f"- El decuento que se hace por no ser del día es del 60%, por lo que se te hace un descuento de -{descuento_ahorrado}€")
    print(f"- El coste total de las barras no frescas es de: {precio_pan_descontado}€")

except ValueError:
    print(f"\nNo se que pan es ese!")