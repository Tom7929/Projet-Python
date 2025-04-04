import zipfile, time
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