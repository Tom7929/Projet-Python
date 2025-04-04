import zipfile, time
print("1 pour un brut force, 2 pour une attaque par dictionnaire")
nombre = input ("que voulez vous faire ? Choisissez le numéro correspondant.")
if nombre == 1:
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

else:

    fichierZip = zipfile.ZipFile("fichiertest.zip")
    fichier_pwd = open("mdp5000fr.txt", 'r') 
    Lignes = fichier_pwd.readlines()
    avant = time.time()
    for mdp in Lignes: # boucle pour tester les mdp du fichier
        mdp = mdp.strip()
    
        try:
            fichierZip.extractall("Extract",pwd=bytes(mdp,"utf-8")) # creer et envoie dans le dossier Extract
            print(mdp," est le bon mdp ! ")
            break
        except:
            print(mdp," n'est pas le bon mdp")

    apres = time.time()
    print("Le temps du test est de : ", apres - avant, "secondes") # temps que la recherche est en cours
    print("Le temps du test est de : ", apres - avant, "secondes") # temps que la recherche est en cours2
print("Que voulez vous faire maintenant : 1 tester le mdp, 2 arrêter le programme")
choix = input ("que voulez vous faire ? Choisissez le numéro correspondant.")
if nombre == 1:
    fichierZip = zipfile.ZipFile("fichiertest.zip")
    fichier_pwd = open("mdp5000fr.txt", 'r') 
    Lignes = fichier_pwd.readlines()

    avant = time.time()

    for mdp in Lignes: # boucle pour tester les mdp du fichier
        mdp = mdp.strip()
        
        try:
            fichierZip.extractall("Extract",pwd=bytes(mdp,"utf-8")) # creer et envoie dans le dossier Extract
            print(mdp," est le bon mdp ! ")
            break
        except:
            print(mdp," n'est pas le bon mdp")

    apres = time.time()
else:
    print("à bientôt")