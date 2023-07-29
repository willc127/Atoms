from atomic_dict import atomic_dict
from electronic_config import configuracao_eletronica
from name_dict import name_dict_ptBR
from classification import classify_element

# Insira o símbolo do elemento desejado
symbol = "Og"

if symbol in atomic_dict:
    print(f"\nElemento: {name_dict_ptBR[symbol]} ({symbol})") # Retorna o nome do elemento
    print(f"Número atômico: {atomic_dict[symbol]}") # Retorna o número atômico
    print(f"Configuração eletrônica: {configuracao_eletronica(atomic_dict[symbol])}") # Retorna a configuração eletrônica
    print(f"Família: {classify_element(configuracao_eletronica(atomic_dict[symbol]), atomic_dict[symbol])}") #Retorna a classificação do elemento
else:
    print(f"Elemento não conhecido: --> {symbol} <-- \nConsulte a tabela periódica e insira um elemento válido.")