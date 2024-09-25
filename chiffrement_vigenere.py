def chiffrement_vigenere(texte: str, cle: str) -> str:
    """Fonction qui chiffre un texte avec la méthode de Vigenère .

    Args:
        texte (str): Texte à chiffrer
        cle (str): clef de chiffrement

    Returns:
        str: Texte chiffré
    """
    texte_chiffre = []
    longueur_cle = len(cle)
    index_cle = 0

    ascii_min = 32
    ascii_max = 126
    intervalle_ascii = ascii_max - ascii_min + 1

    for caractere in texte:
        ascii_caractere = ord(caractere)
        
        if ascii_min <= ascii_caractere <= ascii_max:
            caractere_cle = cle[index_cle % longueur_cle]
            ascii_cle = ord(caractere_cle)
            
            ascii_chiffre = (ascii_caractere - ascii_min + (ascii_cle - ascii_min)) % intervalle_ascii + ascii_min
            caractere_chiffre = chr(ascii_chiffre)
            
            texte_chiffre.append(caractere_chiffre)
            index_cle += 1
        else:
            texte_chiffre.append(caractere)
    
    return ''.join(texte_chiffre)