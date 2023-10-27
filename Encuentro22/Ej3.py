"""Crear una función que tome como argumento un número entero. Es número va a indicar la
cantidad de términos a calcular de la secuencia Fibonacci y devuelva una lista.

La función debe chequear que el argumento que le pasamos sea mayor a 2. En caso de ser
menor, devuelve un mensaje y termina la operacion."""

def fibo(n):
    if n <= 2:
        return "El número debe ser mayor que 2."
        
    fibonacci = [0, 1]
    
    while len(fibonacci) < n:
        next = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next)
    
    return fibonacci

prueba = 10  
resultado = fibo(prueba)
print(resultado)

