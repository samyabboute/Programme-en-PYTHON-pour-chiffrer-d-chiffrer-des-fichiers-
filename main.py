#Programme pour chiffrer/déchiffrer des fichiers 
#CE PROGRAMME UTILISE UNE METHODE DE CHIFFREMENT TRES BASIQUE ^^XOR^^
#Créer par: Samy ABBOUTE 
from hashlib import sha256 
entree  =   input("entrez le nom du fichier à chiffrer/déchiffrer : ")
sortie  =   input("entrez le nom du fichier final : ")
key  =   input("entrez votre clé :  ")
keys = sha256(key.encode('utf-8')).digest()
with open(entree,'rb') as f_entree:
    with open(sortie,'wb') as f_sortie:
        i=0
        while f_entree.peek():
            c = ord(f_entree.read(1))
            j =   i % len(keys)
            b = bytes([c^keys[j]])
            f_sortie.write(b)
            i=i+1
