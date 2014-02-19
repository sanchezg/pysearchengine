'''
Created on 19/02/2014

@author: gsanchez
@description: Motor de busqueda e identificacion de productos, cateogrias y marcas.
'''

import time

'''
listado de palabras que quiero descartar
'''
pal_comunes = ['los','las','sin','con','tan','por']
lista_categorias = ['lacteos','comestibles','auto','hogar']
lista_productos = ['leche','huevo','aceite','yerba']
lista_marcas = ['sandor','la serentisima','mr egg','amandla']
lista_unidad = ['litro','kilo','gramos']
lista_descripcion = ['medio','extra calcino','16','veinte']


'''
Devuelve una lista de posibles marcas detectadas
'''
def marcas_detectadas(lista_terminos):
    ret_marcas_lista = []
    for pal in lista_terminos:
        for marca in lista_marcas:
            #tupla de termino y marca, algunas 'marcas' tienen mas de una palabra
            if marca.find(pal) > -1:
                ret_marcas_lista.append(marca)
    print 'marcas: ', ret_marcas_lista
    return ret_marcas_lista

'''
Devuelve una lista de posibles productos detectadas
'''
def productos_detectados(lista_terminos):
    ret_prod_lista = []
    for pal in lista_terminos:
        if pal in lista_productos:
            ret_prod_lista.append(pal)
    print 'productos: ',ret_prod_lista
    return ret_prod_lista

'''
Descarta palabras que son menores a 3 letras o sean comunes
'''
def item_ok(pal):
    if (pal.isalpha() and len(pal) < 3) or pal in pal_comunes:
        return False
    return True

'''
Para una busqueda concreta devuelve una tupla de producto y categoria
'''
def parse_items(arg_lista):
    lista_pal=arg_lista.split()
    #filtrar palabras que no interesan
    lista_final = filter(item_ok, lista_pal)
    #remover palabras duplicadas
    set_lista = set()
    resultado = []
    for item in lista_final:
        if item not in set_lista:
            set_lista.add(item)
            resultado.append(item)
    #lista_final = list(set(lista_final))
    marcas_detectadas(resultado)
    productos_detectados(resultado)
    print resultado

'''
Programa ejemplo de uso
'''
if __name__ == '__main__':
    start_time = time.time()
    parse_items('hola que tal necesito comprar una leche marca la serentisima o la sandor para saber si esta en buen precio la de 1 litro y tambien una yerba de medio kilo marca amandla')
    print 'execution time: ', time.time() - start_time, 'seconds'