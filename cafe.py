tem_agua = False
colheres_de_cafe = 2

if tem_agua == False:
    print("Adicionando água no reservatório...")
    tem_agua = True

if colheres_de_cafe > 0:
    print("Colocando o pó no filtro...")
    print("Ligando a máquina...")
    print("Seu café está pronto! Tenha um bom dia!")
else:
    print("Não há café suficiente para preparar a bebida. Por favor, adicione mais pó de café.")
    print("Erro crítico: Faltou café na despensa. A operação falhou.")