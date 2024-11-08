def es_primo(num):
    EPSILON = 1e-10
    
    # Explicit check for boolean values
    if isinstance(num, bool):
        raise TypeError("El argumento debe ser un número entero")
    
    if not isinstance(num, (int, float)):
        raise TypeError("El argumento debe ser un número entero")
    
    if isinstance(num, float):
        nearest_int = round(num)
        if abs(num - nearest_int) <= EPSILON:
            num = nearest_int
        else:
            raise TypeError("El argumento debe ser un número entero o muy cercano a un entero")
    
    if num < 2:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

if __name__ == "__main__":
    print(es_primo(5))
