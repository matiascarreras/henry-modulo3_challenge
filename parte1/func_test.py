import pytest

from func import es_primo

import pytest
from func import es_primo

# Validación de Números Primos Conocidos
@pytest.mark.parametrize("prime_number", [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31
])
def test_prime_numbers(prime_number):
    assert es_primo(prime_number) is True, f"Failed for prime number: {prime_number}"

# Validación de Números No Primos Conocidos
@pytest.mark.parametrize("non_prime_number", [
    0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20
])
def test_non_prime_numbers(non_prime_number):
    assert es_primo(non_prime_number) is False, f"Failed for non-prime number: {non_prime_number}"

# Manejo de Números Negativos
@pytest.mark.parametrize("negative_number", [
    -1, -2, -3, -5, -11, -13
])
def test_negative_numbers(negative_number):
    assert es_primo(negative_number) is False, f"Failed for negative number: {negative_number}"

# Eficiencia con Números Grandes
@pytest.mark.parametrize("big_number, expected", [
    (1000003, True),   # Known large prime number
    (1000004, False),  # Non-prime large number
    (104729, True),    # Another large prime
    (104730, False)    # Non-prime large number
])
def test_large_numbers(big_number: int, expected: bool):
    assert es_primo(big_number) is expected

@pytest.mark.parametrize("very_large_prime", [
    999983,  # Largest prime under 1 million
    1000003  # First prime over 1 million
])
def test_specific_large_primes(very_large_prime: int):
    assert es_primo(very_large_prime) is True

# Manejo de Entradas No Enteras
@pytest.mark.parametrize("invalid_input", [
    2.3,        # float
    3.9,        # float
    "tres",     # string
    None,       # None
    True,       # boolean
    False,      # boolean
    [1, 2, 3],  # list
    (1,),       # tuple
    {1}         # set
])
def test_invalid_input_types(invalid_input):
    with pytest.raises(TypeError) as excinfo:
        es_primo(invalid_input)
    assert "El argumento debe ser un número entero" in str(excinfo.value)

# Manejo de Inputs Inusuales
@pytest.mark.parametrize("unusual_input, expected_message", [
    ("cinco", "El argumento debe ser un número entero"),
    (None, "El argumento debe ser un número entero"),
    ([], "El argumento debe ser un número entero"),
])
def test_unusual_inputs(unusual_input, expected_message):
    with pytest.raises(TypeError) as excinfo:
        es_primo(unusual_input)
    assert expected_message in str(excinfo.value)

# Additional specific tests for clarity
def test_string_input():
    with pytest.raises(TypeError) as excinfo:
        es_primo("cinco")
    assert "El argumento debe ser un número entero" in str(excinfo.value)

def test_none_input():
    with pytest.raises(TypeError) as excinfo:
        es_primo(None)
    assert "El argumento debe ser un número entero" in str(excinfo.value)

def test_empty_list_input():
    with pytest.raises(TypeError) as excinfo:
        es_primo([])
    assert "El argumento debe ser un número entero" in str(excinfo.value)

# Precisión en Punto Flotante
@pytest.mark.parametrize("almost_prime", [
    19.000000000000004,
    23.000000000000004,
    2.0000000000000004,
    3.0000000000000004,
    5.000000000000001,
    7.000000000000001,
    11.000000000000002
])
def test_almost_integer_primes(almost_prime):
    assert es_primo(almost_prime) is True

@pytest.mark.parametrize("not_close_enough", [
    19.1,
    23.2,
    5.5,
    7.3,
    11.7
])
def test_not_close_enough_numbers(not_close_enough):
    with pytest.raises(TypeError) as excinfo:
        es_primo(not_close_enough)
    assert "debe ser un número entero o muy cercano a un entero" in str(excinfo.value)