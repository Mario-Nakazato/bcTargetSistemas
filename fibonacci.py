def checkFibonacci(num):
    x, y = 0, 1
    while y < num:
        x, y = y, x + y
    if y == num:
        print(f"{num} pertence à sequência de Fibonacci.")
    else:
        print(f"{num} não pertence à sequência de Fibonacci.")

n = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
checkFibonacci(n)