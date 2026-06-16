def soma2(v1:float, v2:float):
    """A função soma2, realiza a  soma entre dois valores
    Args:
        v1(float): Passe um número inteiro ou decimal
        v2(float): Passe um número inteiro ou decimal
    Returns:
        float: Retorna o resultado da  soma entre dois valores
    """

    return v1 + v2

def resto(v1:int, v2: int):
    """A função resto retorna o resto da divisão entre dois valores inteiros
    Args:
        v1(int): Passe um número inteiro que será o dividendo
        v2(int): Passe um número inteiro que será o divisor
    Returns: 
        int: Retorna o resto da divisão entré números
    """

    return v1 % v2

def retornaPorcentagem(v1:float):
    """A função retorna porcentagem, recebe um valor decimal e retorna
    o mesmo valor em porcetagem. Por exemplo: Você passa o valor 6 ou 6.5
    e ele retornará 0.06 e 0.65 respectivamente
    Args:
        v1(float): Passe um número decimal
    Returns:
        float: Retorna o valor em porcentagem
    """

    return v1 / 100

