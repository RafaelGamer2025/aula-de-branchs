import math
import random

def gerar_fibonacci(n):
    """Gera a sequência de Fibonacci com n elementos."""
    fib = [1, 1]
    for _ in range(n - 2):
        fib.append(fib[-1] + fib[-2])
    return fib

def desenhar_espiral_aurea(largura=70, altura=35):
    """
    Desenha a Espiral Logarítmica (Proporção Áurea) em 2D usando matriz ASCII e aleatoriedade.
    """
    # Matriz para a tela em terminal
    grid = [[" " for _ in range(largura)] for _ in range(altura)]
    
    # Caracteres variados para renderizar o traço e o ruído da figura
    simbolos_traco = ["█", "▓", "#", "@", "%", "&", "$", "*"]
    simbolos_suaves = [".", ":", "+", "·", "~"]
    
    # Parâmetros da Espiral Áurea: r = a * e^(b * theta)
    phi = (1 + 5 ** 0.5) / 2
    b = math.log(phi) / (math.pi / 2)
    a = 0.6
    
    # Centro da imagem na matriz
    cx = largura // 2
    cy = altura // 2
    
    # Ajuste de proporção para compensar a altura do caractere do terminal
    aspect_ratio = 2.1 
    
    # Renderização da espiral ponto a ponto
    theta = 0.0
    passo_theta = 0.03
    theta_maximo = 4.2 * math.pi
    
    while theta < theta_maximo:
        r = a * math.exp(b * theta)
        
        # Conversão de coordenadas polares para cartesianas
        x = cx + int(r * math.cos(theta) * aspect_ratio)
        y = cy + int(r * math.sin(theta))
        
        # Desenha a linha principal
        if 0 <= x < largura and 0 <= y < altura:
            grid[y][x] = random.choice(simbolos_traco)
            
            # Adiciona partículas aleatórias ao redor para dar efeito visual de densidade
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < largura and 0 <= ny < altura and grid[ny][nx] == " ":
                        if random.random() < 0.25:
                            grid[ny][nx] = random.choice(simbolos_suaves)
        
        theta += passo_theta

    # Impressão da moldura e da figura gerada
    print("┌" + "─" * largura + "┐")
    for linha in grid:
        print("│" + "".join(linha) + "│")
    print("└" + "─" * largura + "┘")

# --- EXECUÇÃO ---

# 1. Gerar e exibir a lista de Fibonacci
quantidade_termos = 12
lista_fibonacci = gerar_fibonacci(quantidade_termos)

print(f"\nLISTA DE FIBONACCI ({quantidade_termos} termos):")
print(lista_fibonacci)
print("\nIMAGEM DA ESPIRAL ÁUREA (ASCII):")

# 2. Desenhar a figura no terminal
desenhar_espiral_aurea(largura=70, altura=35)