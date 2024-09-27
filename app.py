from models.sub_algorithms import universal_input, media_checkpoint, media_sprints, media_semester

print(f'--------------------------  PRIMEIRO SEMESTRE')

# Entrada de dados dos checkpoints e a sua Média
checkpoints = universal_input('checkpoint', 3)
MCP1Sem = media_checkpoint(checkpoints)
print(f'\nMédia dos checkpoints: {MCP1Sem}')

# Entrada de dados das Sprints e a sua Média
sprints = universal_input('sprint', 2)
MS1Sem = media_sprints(sprints)
print(f'\nMédia dos sprints: {MS1Sem}')

# Entrada do dado da Prova Semestral
GS1Sem = universal_input('prova semestral', 1)
GS1Sem = GS1Sem[0]

# Média ponderada do (1º) primeiro semestre
weighting = {'MCPSem': 2, 'MSSem': 2, 'GSSem': 6}
first_semester_averages = {'MCPSem': MCP1Sem, 'MSSem': MS1Sem, 'GSSem': GS1Sem}
M1Sem = media_semester(weighting, first_semester_averages)
print(f'\nMédia do primeiro semestre {M1Sem:.2f}')

print(f'--------------------------  SEGUNDO SEMESTRE')
