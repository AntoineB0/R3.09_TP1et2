import Kasiski as K

def kasiski_multi_longueur(texte: str) -> None:
    """On va appeler la fonction kasiski avec differents longueur et si le pgcd est le meme alors on a la longueur de la cle

    Args:
        texte (str): Texte que l'on veut analyser

    Returns:
        None: Affiche les pourcentages d'apparition des chiffres trouvés
    """
    tableau_pgcd = []
    for i in range(4, 10):
        pgcd = K.kasiski(texte, i)
        tableau_pgcd.append(pgcd)
    
    #statistique apparition dans le tableau pcgd
    occurrences = {}
    for pgcd in tableau_pgcd:
        if pgcd in occurrences:
            occurrences[pgcd] += 1
        else:
            occurrences[pgcd] = 1
    
    # Longueur totale du tableau
    total_elements = len(tableau_pgcd)

    # Calculer les pourcentages d'apparition
    pourcentages = {element: (count / total_elements) * 100 for element, count in occurrences.items()}

    # Afficher le résultat
    for element, pourcentage in pourcentages.items():
        print(f"Chiffre {element}: {pourcentage:.2f}% d'apparition")
        
