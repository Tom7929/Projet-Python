import time

listecaractère="abcdefghijklmnopqrstuvwxyz0123456789" # liste de caractères
def generer_mot_recursive(x,prefixe=""):
    if x == 0:
        return [prefixe]
    mots = []
    for carac in listecaractère:
        mots += generer_mot_recursive (x-1, prefixe + carac)
    return mots

avant = time.time() 

tailleMots = 5 # indiquez le nombre de caractère
liste_mot = generer_mot_recursive (tailleMots)
apres = time.time()
print("Les mdp ont étés envoyés vers le fichier : résultats.txt, cela a durer : ", apres - avant, "secondes") # temps que la recherche est en cours


fichier = open("resultats.txt", "w")
for mots in liste_mot:
    fichier.write(mots + "\n")
fichier.close()
