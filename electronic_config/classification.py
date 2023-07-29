def classify_element(elec_config, atomic_number):
    fim_elec_config = elec_config[-3:-1]
    classification_dict = {
        's¹': 'Metal alcalino',
        's²': 'Metal alcalino-terroso',
        'p¹': 'Boro',
        'p²': 'Carbono',
        'p³': 'Pnictogênio',
        'p⁴': 'Calcogênio',
        'p⁵': 'Halogênio',
        'p⁶': 'Gás nobre'
    }
    classification = classification_dict.get(fim_elec_config, '')

    if fim_elec_config[-2] == 'd':
        classification = 'Metal de transição'
    elif 57 <= atomic_number <= 70:
        classification = 'Lantanídeo'
    elif 89 <= atomic_number <= 102:
        classification = 'Actnídeo'

    return classification
