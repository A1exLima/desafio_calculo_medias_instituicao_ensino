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
first_semester_weighting = {'MCPSem': 2, 'MSSem': 2, 'GSSem': 6}
first_semester_averages = {'MCPSem': MCP1Sem, 'MSSem': MS1Sem, 'GSSem': GS1Sem}
M1Sem = media_semester(first_semester_weighting, first_semester_averages)
print(f'\nMédia do primeiro semestre {M1Sem:.2f}')

print(f'\n--------------------------  SEGUNDO SEMESTRE')

# Entrada de dados dos checkpoints e a sua Média
checkpoints = universal_input('checkpoint', 3)
MCP2Sem = media_checkpoint(checkpoints)
print(f'\nMédia dos checkpoints: {MCP2Sem}')

# Entrada de dados das Sprints e a sua Média
sprints = universal_input('sprint', 2)
MS2Sem = media_sprints(sprints)
print(f'\nMédia dos sprints: {MS2Sem}')

# Entrada do dado da Prova Semestral
GS2Sem = universal_input('prova semestral', 1)
GS2Sem = GS2Sem[0]

# Média ponderada do (2º) segundo semestre
second_semester_weighting = {'MCPSem': 2, 'MSSem': 2, 'GSSem': 6}
second_semester_averages = {'MCPSem': MCP2Sem, 'MSSem': MS2Sem, 'GSSem': GS2Sem}
M2Sem = media_semester(second_semester_weighting, second_semester_averages)
print(f'\nMédia do segundo semestre {M2Sem:.2f}')