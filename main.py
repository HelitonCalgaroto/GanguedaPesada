# 5) Desenvolva um programa que receba do usuário o nome completo de uma pessoa e retorne
# como saída uma versão reduzida deste nome, substituindo, se necessário, nomes do meio e
# sobrenomes por sua inicial, de forma que ele passe a ter no máximo 25 caracteres, observando
# as seguintes regras:

# • Conectores (da, do, de, e) não são abreviados, e aqueles que ficarem entre
# abreviações deverão ser desconsiderados.

# Exemplos:
# Entrada: Alberto Moura da Silva Pereira
# Saída: Alberto M S Pereira
# Entrada: João Carlos Albuquerque
# Saída: João Carlos Albuquerque
# Entrada: Maria Aparecida de Lima Soares
# Saída: Maria A de Lima Soares

from valid_First_Name import valid_First_Name

name = input("Informe o nome do indivíduo: ").split(" ")

name = valid_First_Name(name)

print(name)

# 12345678911131517192123 da nunes do silva 2527