def validate_character(value):
    validate = all(char.isdigit() or char == '.' for char in value)


    if validate == True:
        note = float(value)
        return note
    else:
        while not validate:
            try:
                note = float(
                    input('Nota inválida.\nDigite um valor numérico entre 0 e 10: '))
                validate = True
                return note
            except ValueError:
                pass


def validate_note(note):
    note = validate_character(note)

    while note < 0 or note > 10:
        try:
            note = float(
                input('Nota inválida.\nDigite um valor numérico entre 0 e 10: '))
        except ValueError:
            pass

    return note


def validation_status(Ma, revalidation=False):
    status = ''

    match Ma:
        case _ if Ma >= 6:
            status = 'Aprovado'

        case _ if Ma <= 4:
            status = 'Reprovado'

        case _ if Ma >= 4 and Ma <= 5.9:
            if revalidation:
                status = f'Aprovado' if Ma >= 6 else f'Reprovado'
            else:
                status = 'Exame'

    return status
