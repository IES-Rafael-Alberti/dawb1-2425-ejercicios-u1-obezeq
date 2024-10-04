#!/usr/bin/env python3 

def titular_v1(frase):
    frase = frase.strip()
    
    nueva_frase = ""
    nueva_palabra = True
    
    for c in frase:
        if c == " ":
            nueva_frase += c
            nueva_palabra = True
        elif nueva_palabra:
            nueva_frase += c.upper()
            nueva_palabra = False
        else:
            nueva_frase += c.lower()
            
    return nueva_frase

def titular_v2(frase):
    frase = frase.strip()
    palabras = frase.split(' ')
    nueva_frase = []
    
    for palabra in palabras:
        if palabra:
            nueva_frase.append(palabra[0].upper() + palabra[1:].lower())
            
    return ' '.join(nueva_frase)

def titular_v3(frase):
    frase = frase.strip()
    palabras = frase.split(' ')
    
    c = 0
    for p in range(len(palabras)):
        if palabras[c] != '':
            palabras[c] = palabras[c][0].upper() + palabras[c][1:].lower()
            c += 1
        else:
            del palabras[c]
            
    return ' '.join(palabras)
    
def main():
    og_frase = input("[+] Introduce una frase: ")
    v1 = titular_v1(og_frase)
    v2 = titular_v2(og_frase)
    v3 = titular_v3(og_frase)
    
    print(f"\nOriginal: {og_frase}")
    print(f"titular_v1: {v1}")
    print(f"titular_v2: {v2}")
    print(f"titular_v3: {v3}")
    
    

if __name__ == '__main__':
    main()