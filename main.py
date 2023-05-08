"""Módulo com funções."""


def is_prime(number: int) -> bool:
    """Retorna True se o número for primo e False caso contrário."""
    for i in range(2, number):
        if(number % i == 0):
            return False
    return True


def list_prime_factors(number: int) -> list[int]:
    """Retorna uma lista com os fatores primos de cada número da lista fornecida."""
    fatores = []
    numero = number
    for i in range(2, number + 1):
        if is_prime(i):
            while numero % i == 0:
                fatores.append(i)
                numero = numero / i
    return fatores

