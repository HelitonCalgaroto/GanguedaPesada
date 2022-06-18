# from abrev_Name import abrev_Name


def valid_Mid_Name(fullname: []) -> []:

    if len(fullname[0]) + len(fullname[-1]) == 25:
        return fullname[0] + " " + fullname[-1]

    elif len(fullname[0]) + len(fullname[-1]) > 25:
        name = len(fullname[0])
        lastName = 0

        while name < 25:
            for i in (fullname[-1]):
                lastName += 1
                name += 1
                if name == 25:
                    break
        return fullname[0] + " " + fullname[-1][:lastName]

    else:
        return abrev_Name(fullname)
