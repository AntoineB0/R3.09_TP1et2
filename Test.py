import chiffrement_vigenere as CV
import déchiffrement_vigenere as DV

import unittest

class TestVigenereCipher(unittest.TestCase):

    def test_chiffrement_simple(self):
        texte = "Bonjour"
        cle = "CLE"
        resultat_attendu = "e<4.<;6"
        self.assertEqual(CV.chiffrement_vigenere(texte, cle), resultat_attendu)

    def test_chiffrement_avec_ponctuation(self):
        texte = "Bonjour, monde!"
        cle = "CLE"
        resultat_attendu = "e<4.<;6XE1<4(2F"
        self.assertEqual(CV.chiffrement_vigenere(texte, cle), resultat_attendu)

    def test_chiffrement_caracteres_speciaux(self):
        texte = "Bonjour123!"
        cle = "CLE"
        resultat_attendu = "e<4.<;6]WVM"
        self.assertEqual(CV.chiffrement_vigenere(texte, cle), resultat_attendu)

    def test_dechiffrement_simple(self):
        texte_chiffre = "e<4.<;6"
        cle = "CLE"
        resultat_attendu = "Bonjour"
        self.assertEqual(DV.déchiffrement_vigenere(texte_chiffre, cle), resultat_attendu)

    def test_dechiffrement_avec_ponctuation(self):
        texte_chiffre = "e<4.<;6XE1<4(2F"
        cle = "CLE"
        resultat_attendu = "Bonjour, monde!"
        self.assertEqual(DV.déchiffrement_vigenere(texte_chiffre, cle), resultat_attendu)

    def test_dechiffrement_caracteres_speciaux(self):
        texte_chiffre = "e<4.<;6]WVM"
        cle = "CLE"
        resultat_attendu = "Bonjour123!"
        self.assertEqual(DV.déchiffrement_vigenere(texte_chiffre, cle), resultat_attendu)

    def test_chiffrement_et_dechiffrement(self):
        texte = "Bonjour, monde! Chiffrement : Vigenere 123."
        cle = "CLE"
        texte_chiffre = CV.chiffrement_vigenere(texte, cle)
        texte_dechiffre = DV.déchiffrement_vigenere(texte_chiffre, cle)
        self.assertEqual(texte_dechiffre, texte)

if __name__ == "__main__":
    unittest.main()
