from palindromo import palindromes
from palindromo import obtener_cantidad_de_palabras_palindromes

def palindromes(word):
    if len(word) <= 1: 
        return True
    if word[0]== word[-1]:
        return palindromes(word[1:-1])
    else: 
        return False
    
print(palindromes("romenar"))


def obtener_cantidad_de_palabras_palindromes(word):
    contador = 0
    for word in word:
        if word == word[::-1]:  
            contador += 1
    return contador  
