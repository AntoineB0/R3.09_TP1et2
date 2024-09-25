# Exercice 1
import chiffrement_vigenere as CV
import déchiffrement_vigenere as DV


def Exemple():
    texte = input("Entrez le texte à chiffrer : ")
    cle = input("Entrez la clé : ")

    texte_chiffre = CV.chiffrement_vigenere(texte, cle)
    print("Texte chiffré :", texte_chiffre)
    
    texte_déchiffré = DV.déchiffrement_vigenere(texte_chiffre, cle)
    print("Texte déchiffré :", texte_déchiffré)



if __name__ == '__main__':
    Exemple()
