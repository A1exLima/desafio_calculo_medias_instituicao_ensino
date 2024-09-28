from models.sub_algorithms import universal_input, media_checkpoint, media_sprints, media_semester, media_annual, average_final_exam_score
from models.validation_algorithms import validation_status


def first_semester():
    global M1Sem
    print(f'\n--------------------------  PRIMEIRO SEMESTRE')

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
    first_semester_averages = {'MCPSem': MCP1Sem,
                               'MSSem': MS1Sem, 'GSSem': GS1Sem}
    M1Sem = media_semester(first_semester_weighting, first_semester_averages)
    print(f'\nMédia do primeiro semestre {M1Sem:.2f}')


def second_semester():
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
    second_semester_averages = {
        'MCPSem': MCP2Sem, 'MSSem': MS2Sem, 'GSSem': GS2Sem}
    M2Sem = media_semester(second_semester_weighting, second_semester_averages)
    print(f'\nMédia do segundo semestre {M2Sem:.2f}')

    # Média ponderada Anual
    average_annual_weighting = {'M1Sem': 4, 'M2Sem': 6}
    semester_averages = {'M1Sem': M1Sem, 'M2Sem': M2Sem}
    Ma = media_annual(average_annual_weighting, semester_averages)

    # Status da média Anual
    status = validation_status(Ma)
    print(f'\nMédia final {Ma:.1f} - {status}!')

    if status == 'Exame':
        Ne = universal_input('nota de exame', 1)
        Ne = Ne[0]
        Mf = average_final_exam_score(Ma, Ne)
        status = validation_status(Mf, revalidation=True)
        print(f'\n{status} em exame com a média {Mf:.2f}.')


def continue_or_stop_program(status):
    continue_program = True if status == 'S' else False
    return continue_program


def main():
    continue_program = True

    while continue_program:
        first_semester()
        second_semester()

        status = input(
            f'\nCalcular a média de outro aluno? [S]im ou [N]ão: ').upper()

        continue_program = continue_or_stop_program(status)

        while status != 'S' and status != 'N':
            status = input('Digite "S" para SIM ou "N" para NÃO: ').upper()
            continue_program = continue_or_stop_program(status)

    print(f'\nObrigado por utilizar o nosso programa!\n')


if __name__ == "__main__":
    main()
