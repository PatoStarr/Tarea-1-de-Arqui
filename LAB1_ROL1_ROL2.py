<<<<<<< Updated upstream
from pathlib import Path
ruta = Path(__file__).parent / "Archivos_prueba/Encriptados/prueba_3.txt"

numeros_convertidos = []

#se vienen los mapas lol
bi_a_hex = {
    "0000":"0","0001":"1","0010":"2","0011":"3",
    "0100":"4","0101":"5","0110":"6","0111":"7",
    "1000":"8","1001":"9","1010":"A","1011":"B",
    "1100":"C","1101":"D","1110":"E","1111":"F"
}

hex_a_bi = {v: k for k, v in bi_a_hex.items()}
#lo de arriba invierte el "mapa"

bi_a_dec = {
    "0000":"00","0001":"01","0010":"02","0011":"03",
    "0100":"04","0101":"05","0110":"06","0111":"07",
    "1000":"08","1001":"09","1010":"10","1011":"11",
    "1100":"12","1101":"13","1110":"14","1111":"15"
}

dec_a_bi = { v: k for k, v in bi_a_dec.items()}

bi_a_oct = {
    "0000":"00","0001":"01","0010":"02","0011":"03",
    "0100":"04","0101":"05","0110":"06","0111":"07",
    "1000":"10","1001":"11","1010":"12","1011":"13",
    "1100":"14","1101":"15","1110":"16","1111":"17"
}

oct_a_bi = { v: k for k, v in bi_a_oct.items()}

oct_a_dec = {
    "00":"00","01":"01","02":"02","03":"03",
    "04":"04","05":"05","06":"06","07":"07",
    "10":"08","11":"09","12":"10","13":"11",
    "14":"12","15":"13","16":"14","17":"15"
}

dec_a_oct = {v: k for k, v in oct_a_dec.items()}

oct_a_hex = {
    "00":"0","01":"1","02":"2","03":"3",
    "04":"4","05":"5","06":"6","07":"7",
    "10":"8","11":"9","12":"A","13":"B",
    "14":"C","15":"D","16":"E","17":"F"
}

hex_a_oct = {v: k for k, v in oct_a_hex.items()}

dec_a_hex = {
    "00":"0","01":"1","02":"2","03":"3",
    "04":"4","05":"5","06":"6","07":"7",
    "08":"8","09":"9","10":"A","11":"B",
    "12":"C","13":"D","14":"E","15":"F"
}

hex_a_dec = {v: k for k, v in dec_a_hex.items()}
#fin mapas


#el nombre dice lo que hará lol
def leer_archivo():
    #texto_valido = ""
    numero = ""
    numeros = []
    inicio = True       #no sabia como abrir el archivo cuando estaba dentro de otro coso lol ksjdksjd
    with open(ruta, 'r', encoding='utf-8') as file:
        contenido = file.read()
    for caracter in contenido:
        #esto se encarga de limpiar las letras o caracteres que no dan informacion lol
        if caracter in "*&!#1234567890ABCDEF":
            #texto_valido = texto_valido + caracter
            if caracter in "1234567890ABCDEF":
                numero = numero + caracter
            elif caracter in "*&#!" and not inicio:
                numeros.append(numero)
                numero = caracter
                #print(numero)
            else: #este else lo puse para que no se saltara el primer numero pe skdjksjd o agregue algo vacio
                numero = numero + caracter
                inicio = False
        else:
            continue
    for numeros in numeros:
        print(numeros)
    print(numero)
    return numeros
    #print(texto_valido)

#esto leera los numeros y dependiendo con que signo empiezen pues lo mandara a la funcion para transformarlos
#o al menos eso quiero que haga lol
def leer_numero(inicio, numeros):
    global numeros_convertidos
    convertido = ""
    """for numero in numeros:
        if inicio == "*":
            convertido = a_bi(numero)
        print(numero)"""
        

    #return None
=======
>>>>>>> Stashed changes





<<<<<<< Updated upstream

def a_hex():

    return None

def a_dec():

    return None

def a_octa():
    return None

def a_bi():
    return None


def main():
    flag = True
    while flag:
        base = input("seleccione la base (2, 8, 10, 16): ")
        if base == "2":
            inicio = "*"
            flag = False
        elif base == "8":
            inicio = "&"
            flag = False
        elif base == "10":
            inicio = "#"
            flag = False
        elif base == "16":
            inicio = "!"
            flag = False
        else:
            print("Entrada invalida: intentar de nuevo")
    numeros = leer_archivo()
    leer_numero(inicio,numeros)

main()
=======
def main():
    archivo=open("notas_dm.txt", "r")
    contenido=archivo.read()
    archivo.close()

    print("---DECODIFICADOR DE NOTAS---\n\n\n")

    base=int(input("Ingrese la base en la que desea visualizar los datos (2, 8, 10, 16): "))

    print("\n\n[+] Procesando archivo: notas_dm.txt...\n")
    print("[!] Filtrando ruido m ıstico (valores fuera de rango ASCII)...\n")

    #hacer funciones para cada base
    #se me ocurre q tmbn se podría hacer como un for para recorrer todo el archivo y 
    #guardar los números en una lista, pero ns como hacerlo :( (por ahora)
    


if __name__=="__main__":
    main()
>>>>>>> Stashed changes
