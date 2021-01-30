import json

#lendo json

content = open('dados.json').read()

pessoas = json.loads(content)

#for pra ficar em loop

for item in pessoas:
    print(item)


# usando uma estrutura similar ao que já conhecemos em migrcoes,
# a ideia seria criar um dataset contendo todos os dados, e ficar
# lupando esse cara acessando cada um dos índices.

