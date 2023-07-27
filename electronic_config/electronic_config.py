def configuracao_eletronica(numero_atomico):

    # Define a codificação para utf-8.
    # Isso permite o sobrescrito da configuração eletrônica
    import sys
    sys.stdout.reconfigure(encoding='utf-8')

    # Define o número máximo de elétrons
    eletrons_restantes = numero_atomico
    configuracao = ""

    # Lista com os orbitais e o número máximo de elétrons em cada um deles
    orbitais = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s',
                '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f', '6d', '7p']
    max_eletrons = [2, 2, 6, 2, 6, 2, 10, 6,
                    2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]

    # Função para converter os números em sobrescrito
    def to_superscript(number):
        superscript_digits = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
        return str(number).translate(superscript_digits)

    # Percorre a lista de orbitais até que eletrons_restantes seja 0
    for i, orbital in enumerate(orbitais):
        if eletrons_restantes <= 0:
            break
        # Verifica se eletrons_restantes é maior que o número máximo de elétrons por orbital
        eletrons_no_orbital = min(eletrons_restantes, max_eletrons[i])
        # Atualiza a quantidade de elétrons restantes
        eletrons_restantes -= eletrons_no_orbital

        # Escreve a configuração eletrônica
        configuracao += f"{orbital}{to_superscript(eletrons_no_orbital)} "

    return configuracao
