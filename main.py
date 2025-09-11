def max_min_select(lista):
    """
    Função principal (Wrapper) que o usuário chama.
    Ela lida com casos especiais e faz a chamada inicial para a função recursiva.
    """
    # Caso 1: Se a lista for vazia, não há maior nem menor.
    if not lista:
        return None, None
    
    # Chama a função recursiva auxiliar, começando a verificação a partir do segundo elemento (índice 1)
    return _max_min_recursivo(lista, 0, len(lista)-1)


def _max_min_recursivo(lista, inicio, fim):
   # CASO BASE 1: Se há apenas um elemento na sublista
    if inicio == fim:
        maior = lista[inicio]
        menor = lista[inicio]
        return maior, menor

    # CASO BASE 2: Se há dois elementos na sublista
    elif inicio == fim - 1:
        if lista[inicio] < lista[fim]:
            maior = lista[fim]
            menor = lista[inicio]
        else:
            maior = lista[inicio]
            menor = lista[fim]
        return maior, menor

    else:
        # 1. DIVIDIR: Achar o meio da sublista atual
        meio = (inicio + fim) // 2
        
        # 2. CONQUISTAR: Chamar recursivamente para as duas metades
        max_esq, min_esq = _max_min_recursivo(lista, inicio, meio)
        max_dir, min_dir = _max_min_recursivo(lista, meio + 1, fim)
        
        # 3. COMBINAR: Encontrar o maior dos dois maiores e o menor dos dois menores
        maior_final = max(max_esq, max_dir)
        menor_final = min(min_esq, min_dir)
        
        return maior_final, menor_final

def main():
    minha_lista = [3, 8, 1, 9, 4, -2, 10, 5, 7]
    maior_elemento, menor_elemento = max_min_select(minha_lista)

    print(f"A lista é: {minha_lista}")
    print(f"Maior elemento: {maior_elemento}") 
    print(f"Menor elemento: {menor_elemento}") 

if __name__ == "__main__":
    main()