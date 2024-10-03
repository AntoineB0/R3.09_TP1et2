
import chiffrement_vigenere as CV
import déchiffrement_vigenere as DV
import KasiskiMultiLongueur as K


def Menu():
    print("-------------------------------")
    print("1.Chiffrement et déchiffrement de Vigenère")
    print("2.Kasiski")
    print("3.Quitter")
    choix = int(input("Entrez votre choix : "))
    if choix == 1:
        texte = input("Entrez le texte à chiffrer : ")
        cle = input("Entrez la clé : ")

        # Exercice 1
        texte_chiffre = CV.chiffrement_vigenere(texte, cle)
        print("Texte chiffré :", texte_chiffre)
        
        #Exercice 2
        texte_déchiffré = DV.déchiffrement_vigenere(texte_chiffre, cle)
        print("Texte déchiffré :", texte_déchiffré)
        input("Appuyez sur entrée pour continuer")
        Menu()
    elif choix == 2:
        #Exercice 3
        texte_TD1 = "XNRDGQZUDNKOPIZTTMRTLKGXPNRLBAOEDFTRBXZAVRRPKQIMAGFRLBNYHCIYSBGZPLPSLAOZRLLDHAZTTSKUGGURHIUEFPGZCECAWBGOZSKHDBJACOKTDZMQIWVANVKEHEJIQBNQRRPPWWMDPPYIFIRSDRZTKUYFWEDSHTBQHBLTLVYFTAUEAXRAXTNEDSTQHSVSLVZTTIIIPXRQBEETDBOACEMEQBNAJGYTKMMAPLYAVJKQCTYEVISQIHVMHBNASSRNGBKOWNZQXMYAUCIYSBGZPLPSLANMKETHDVMQSDIAVBOOPLCYWPXAJGYTKMNUHTFRBWLOGYGTROXMEHPAGIVFXNXTRQTOGERSLVMOGYGTROXMEHZCFWSBAEOIWGXMCGZNJNXABTYESMTMCDGASMXYTTYOGAURIHVPDAZFWRFUJPSMRHZNHARUZEKHHJXUIIJHEWSNTSRNGKUXDSJUVKUYEUKEUAGFQLVTFPRQNPRRNQTIDRCDZIXUXTFTKMSMIHVMDBOOPLCYDLBMCCVDFWSBJTVRLHKPHCYEPMYAUTYESZKETNKMHBNASSWOUJXQPKZNJUUPTRECUGVFDSPSWMSEDFKEQQTHDLMEVWRHXNXCDZKRJLCYFWTEIRLCWMJBGOSLHUYUCPLRHUGFWEDAWQIEIHVBAHAZWCONNEMOZVIETHOKDUATTRZOLPTZOQ"
        K.kasiski_multi_longueur(texte_TD1)
        input("Appuyez sur sur entrée pour continuer")
        Menu()
    elif choix == 3:
        exit()
    else:
        print("Choix invalide")
        Menu()

if __name__ == '__main__':
    Menu()
