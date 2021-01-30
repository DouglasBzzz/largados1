import json
import pandas as pd

#lendo json

content = open('dados.json').read()

json_do_pandas = pd.read_json(r'dados.json')

pessoas = json.loads(content)

#for pra ficar em loop

for item in pessoas:
    print(item)
    
print("--------------------------------------------------")

#print(json_do_pandas)

print(json_do_pandas.info())

#for item2 in json_do_pandas:
#    print(f'Nome: {item2[nome]}')


# usando uma estrutura similar ao que já conhecemos em migrcoes,
# a ideia seria criar um dataset contendo todos os dados, e ficar
# lupando esse cara acessando cada um dos índices.

