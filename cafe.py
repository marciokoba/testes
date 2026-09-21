tem_agua = False
colheres_de_cafe = 2

if tem_agua == False:
    print("Adicionando água no reservatório...")
    tem_agua = True

if colheres_de_cafe > 0:
    print("Colocando o pó no filtro...")
    print("Ligando a máquina...")
    print("Seu café está pronto!")
else:
    print("Erro crítico: Faltou café na despensa. A operação falhou.")