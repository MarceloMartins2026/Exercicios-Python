def acrescimo(preco: float , taxa: float):
    """A função acréscimo realiza o cálculo de aumento
    do valor do preço do produto de acordocom a taxa
    
    Args:
        preço(float): Passe o preço do produto
        taxa(float): Passe a taxa do acréscimo somente número

    Returns:
        float: Retorna o preço do produto com o valor de acréscimo

    """
    return preco * (1+(taxa) / 100)


rs = acrescimo(2560.90, 8.9)

print(f"O valor final do produto é{rs}")

