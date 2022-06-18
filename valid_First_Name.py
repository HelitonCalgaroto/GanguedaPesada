from valid_Mid_Name import valid_Mid_Name


def valid_First_Name(name: []) -> str:

    if len(name[0]) == 25:
        return name[0]

    elif len(name[0]) > 25:
        return name[0][:25]

    else:
        return valid_Mid_Name(name)
