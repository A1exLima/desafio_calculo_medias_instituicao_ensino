from models.validation_algorithms import validate_note


def check_pronoun(name):
    checklist = ['checkpoint', 'sprint']

    if name in checklist:
        personal_pronoun = 'o'
        return personal_pronoun
    else:
        personal_pronoun = 'a'
        return personal_pronoun


def universal_input(name_input, quantity_of_inputs):
    inputs = []

    for i in range(1, quantity_of_inputs + 1):
        inputs.append(
            validate_note(
                input(
                    f'\nDigite {check_pronoun(name_input)} {name_input}'
                    f'{": " if quantity_of_inputs == 1 else f" {i}: "}'
                )
            )
        )
    return inputs


def media_checkpoint(array_checkpoints):
    array_checkpoints.remove(min(array_checkpoints))
    media_checkpoint = sum(array_checkpoints) / len(array_checkpoints)
    return media_checkpoint


def media_sprints(array_sprints):
    media_sprints = sum(array_sprints) / len(array_sprints)
    return media_sprints


def media_semester(weighting, averages):
    MSem = (
        (averages.get('MCPSem') * weighting.get('MCPSem')) +
        (averages.get('MSSem') * weighting.get('MSSem')) +
        (averages.get('GSSem') * weighting.get('GSSem'))
    ) / sum(weighting.values())

    return MSem

def media_annual(weighting, averages):
    Ma = (
        (averages.get('M1Sem') * weighting.get('M1Sem')) +
        (averages.get('M2Sem') * weighting.get('M2Sem'))
    ) / sum(weighting.values())

    return Ma

def average_final_exam_score(Ma, Ne):
    Mf = (Ma + Ne) / 2
    return Mf