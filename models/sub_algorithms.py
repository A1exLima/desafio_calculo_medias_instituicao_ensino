from models.validation_algorithms import validate_note

def checkPointInput():
    CP1 = validate_note(input(f'\nDigite o checkpoint 1: '))
    CP2 = validate_note(input(f'\nDigite o checkpoint 2: '))
    CP3 = validate_note(input(f'\nDigite o checkpoint 3: '))

    return CP1, CP2, CP3