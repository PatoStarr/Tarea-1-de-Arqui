
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
    for num in numeros:
        print(num)
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

#creo q deberia crear funciones para cada conversion
#parece que todas las converiones que impliquen la base decimal no se pueden hacer con los mapas :(


def binario_a_decimal(bin_str):
    decimal=0

    #hacemos un recorrido invertido del numero binario
    for i, digito in enumerate(reversed(bin_str)):  #10
        decimal+=int(digito)*(2**i)
    
    return decimal



def decimal_a_binario(dec_str):
    
    if int(dec_str)==0:
        return 0
    
    bin_str=""
    while int(dec_str)>0:
        bin_str=int(dec_str)%2+bin_str
        int(dec_str)//=2
    
    return bin_str

def hexadecimal_a_decimal(hex_str):
    
    #voy a poner digitos hexadecimales para después usar su posicion como su valor
    digitos_hex="0123456789ABCDEF"

    decimal=0
    #voy a recorrer el hexadecimal al reves
    for i, digito in enumerate(reversed(hex_str)):
        decimal+=digitos_hex.index(i)*(16**i)
    
    return decimal

def decimal_a_hexadecimal(dec_str):
    #voy a convertir dec_str a int
    dec_int=int(dec_str)

    if dec_int==0:
        return 0
    
    digitos_hex="0123456789ABCDEF"
    hexa=""

    while dec_int>0:
        resto=dec_int%16
        hexa=digitos_hex[resto]+hexa
        dec_int//=16
    
    return hexa

#en el libro no sale nada de los numeros octales(creo),pero supongo que la logica de conversion
#debe ser la misma que con binario y hexadecimal
def octal_a_decimal(oct_str):
    decimal=0

    for i, digito in enumerate(reversed(oct_str)):
        decimal+=int(digito)*(8**i)
    
    return decimal

def decimal_a_octal(dec_str):
    dec_int=int(dec_str)
    if dec_int==0:
        return 0
    
    oct=0

    while dec_int>0:
        oct+=dec_int%8
        dec_int//=8
    
    return oct

#ahora voy a codear las funciones que sí se pueden hacer utilizando los mapas
#que son: bin <--> oct, oct<-->hex, bin<-->hex

def binario_a_hexadecimal(bin_str):
    #tenemos que asegurar que el largo del numero binario sea multiplo de 4
    #si no es mult de 4 le agregamos 0's a la izquierda
    #cero a la izquierda JKSAJDKADSBJ XDDDDDD
    while len(bin_str)%4!=0:
        bin_str='0'+bin_str

    hexa=""

    for i in range(0, len(bin_str,4)):
        #vemos por grupos de 4 bits de izq a der
        grupo=bin_str[i:i+4]
        hexa+=bi_a_hex[grupo]
    
    #luego eliminamos los 0's de la izquierda
    hexa=hexa.lstrip('0')
    
    return hexa

def hexadecimal_a_binario(hex_str):
    binario=""

    for digito in hex_str:
        binario=hex_a_bi[digito]+ binario
    
    binario=int(binario)
    return binario

#esta conversion es similar a la de bin a hexa
def binario_a_octal(bin_str):

    #hay q aseguararse de que el largo del num binario sea multiplo de 3
    while len(bin_str)%3!=0:
        bin_str='0'+bin_str
    
    octa=""
    #convertimos en grupos de 3 bits de izq a der
    for i in range(0, len(bin_str),3):
        grupo=bin_str[i:i+3]
        octa=bi_a_oct[grupo]+bin_str
    
    return octa
    
def octal_a_binario(octa_str):
    binario=""
    for digito in octa_str:
        binario=oct_a_bi[digito+binario]
    
    return int(binario)


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



if __name__=="__main__":
    main()

