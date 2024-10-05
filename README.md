# R3.09_TP1et2
R3.09_TP1et2
![alt text](https://github.com/AntoineB0/R3.09_TP1et2/blob/main/Banner_Cryptographie_TP1_2.png)



## Exercice 1 : Chiffrement de Vigenère

### Test 1
- Entrée : `"Bonjour"`
- Clé : `"CLE"`
- Sortie attendue : `"e<4.<;6"`

### Test 2
- Entrée : `"Bonjour, monde!"`
- Clé : `"CLE"`
- Sortie attendue : `"e<4.<;6XE1<4(2F"`

### Test 3
- Entrée : `"Bonjour123!"`
- Clé : `"CLE"`
- Sortie attendue : `"e<4.<;6]WVM"`

## Exercice 2 : Déchiffrement de Vigenère

### Test 4 : Déchiffrement simple
- Entrée : `"e<4.<;6"`
- Clé : `"CLE"`
- Sortie attendue : `"Bonjour"`

### Test 5 : Déchiffrement avec ponctuation
- Entrée : `"e<4.<;6XE1<4(2F"`
- Clé : `"CLE"`
- Sortie attendue : `"Bonjour, monde!"`

### Test 6 : Déchiffrement avec caractères spéciaux
- Entrée : `"e<4.<;6]WVM"`
- Clé : `"CLE"`
- Sortie attendue : `"Bonjour123!"`

### Test 7 : Chiffrement et Déchiffrement
- Entrée : `"Bonjour, monde! Chiffrement : Vigenere 123."`
- Clé : `"CLE"`
- Sortie attendue après chiffrement puis déchiffrement : `"Bonjour, monde! Chiffrement : Vigenere 123."`

## Exercice 3 : Trouver la taille de la clé avec Kasiski
- Entrée : `Texte_TD1.txt`
    - J'ai choisi ce texte car c'est celui sur lequel on a travailler durant le premier TD
    - Durant le TD la taille de la clé trouver été 8
- Sortie : `"Chiffre 8: 100.00% d'apparition"`
