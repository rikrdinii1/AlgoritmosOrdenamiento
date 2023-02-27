import random

def ordenamiento_por_mezcla(lista):

    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]

        # Llamada recursiva en cada mitad
        ordenamiento_por_mezcla(izquierda)
        ordenamiento_por_mezcla(derecha)

        # Iteradores para recorrer las dos sublistas
        i = 0 
        j = 0
        # Iterador para la lista principal
        k = 0

        # Generamos las primeras comparaciones de las dos listas
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1
        
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

    return lista
            




if __name__ == '__main__':
    tamano_lista = int(input('Indque el tamano de la lista: '))

    lista = [random.randint(0,100) for i in range(tamano_lista)]
    print(lista)
    print('-' * 30)

    lista_ordenada = ordenamiento_por_mezcla(lista)
    print(lista_ordenada)