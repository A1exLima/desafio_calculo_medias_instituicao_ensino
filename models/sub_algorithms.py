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
