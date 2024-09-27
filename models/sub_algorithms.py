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
    sum_weighting = sum(weighting.values())

    MSem = (
        (averages[0] * weighting.get('W_MCPSem')) +
        (averages[1] * weighting.get('W_MSSem')) +
        (averages[2] * weighting.get('W_GSSem'))
    ) / sum_weighting

    return MSem
