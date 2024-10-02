def titular(frase):
    frase = frase.split(' ')
    parsed_frase = []
    for w in frase:

        if w != '':
    
            first_letter = w[0].upper()
            last_letter = w[-1]
            mid_letter = w[1:-1]
            
            letters = f"{first_letter}{mid_letter}{last_letter}"
            parsed_frase.append(letters)
    
            frase = ""

    for pw in parsed_frase:
        frase = frase + pw + " "
    frase = frase[:-1]

    print(frase)
        
    
def main():
    titular("   hola mundo desde python   ")

if __name__ == '__main__':
    main()