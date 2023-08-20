nom_fichier_1 = input("Entrez le nom du premier fichier: ")
nom_fichier_2 = "copie-ahh.txt"
with open('ahh.txt', "r") as f1: 
    with open("copie-ahh.txt", "w") as f2:
      for ligne in f1:
              f2.write(ligne.upper())


