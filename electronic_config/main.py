from atomic_dict import atomic_dict
from electronic_config import configuracao_eletronica
from name_dict import name_dict_ptBR

# Insira o símbolo do elemento desejado
symbol = "Og"

if symbol in atomic_dict:
    print(f"Elemento: {name_dict_ptBR[symbol]} ({symbol})")
    print(f"Número atômico: {atomic_dict[symbol]}")
    print(f"Configuração eletrônica: {configuracao_eletronica(atomic_dict[symbol])}")
else:
    print(f"Elemento não conhecido: --> {symbol} <-- \nConsulte a tabela periódica e insira um elemento válido.")