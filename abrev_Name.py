# Entrada: Alberto Moura da Silva Pereira
def abrev_Name(fullname: []) -> str:
    finalname = len(fullname[0]) + len(fullname[-1])

    while finalname > 25:
        for i in range(1, len(fullname) - 1):
            if i > 2:
                if finalname + len(i) >= 25:
