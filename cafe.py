# 1. Variáveis de entrada
tem_agua = True
colheres_de_cafe = 2
opcao_acucar = "com açúcar"
temperatura_agua = 90  # Em graus Celsius (Ideal: entre 90°C e 96°C)

print("--- INICIANDO MÁQUINA DE CAFÉ V3 ---")

# 2. Verificação de água e temperatura
if not tem_agua:
    print("Adicionando água no reservatório...")
    tem_agua = True

if temperatura_agua < 90:
    print("Aquecendo a água até a temperatura ideal...")
    temperatura_agua = 93

# 3. Preparo do café
if colheres_de_cafe > 0:
    print(f"Passando o café a {temperatura_agua}°C...")
    print(f"Servindo café {opcao_acucar}!")
    print("☕ Seu café perfeito está pronto!")
else:
    print("Erro crítico: Faltou café na despensa.")
    print("Erro crítico: Faltou café na despensa. A operação falhou.")