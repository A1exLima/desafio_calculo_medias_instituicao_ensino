def validate_character(value):
    validate = value.isdigit()

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
