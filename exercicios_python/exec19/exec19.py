frase = input("Digite a frase:")

new_frase = frase.replace(" ","")
new_frase_converted = new_frase[::-1]

if new_frase == new_frase_converted:
    print("Palindromo")
else:
    print("Não Palindromo")
