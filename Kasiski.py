from math import gcd

def kasiski(texte: str, longueur: int) -> int:
    """Fonction qui permet de trouver la longueur de la clé de chiffrement d'un texte chiffré avec la méthode de Vigenère.

    Args:
        texte (str): Texte que l'on veut analyser
        longueur (int): Longueur des sous-chaînes à analyser

    Returns:
        int: Longueur de la clé de chiffrement
    """
    repet: dict[str, list[int]] = {}
    sous_chaine: str

    positions: list[int]

    distances: list[int]

    pgcd: int

    for i in range(len(texte) - longueur):
        sous_chaine = texte[i:i + longueur]
        if sous_chaine in repet:
            repet[sous_chaine].append(i)
        else:
            repet[sous_chaine] = [i]

    distances = []
    for sous_chaine in repet:
        positions = repet[sous_chaine]
        if len(positions) > 1:
            for j in range(1, len(positions)):
                distances.append(abs(positions[j] - positions[j - 1]))

    distances = list(dict.fromkeys(distances))
    pgcd = gcd(*distances)

    return pgcd

