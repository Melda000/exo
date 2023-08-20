
nom_fichier_1 = input("Entrez le nom du premier fichier: ")
nom_fichier_2 = "copie_ahh.txt" 
num = 1
with open("ahh.txt", "r") as f1: 
    with open("copie_ahh.txt", "w") as f2:
     for ligne in f1:
            f2.write(str(num) + ". ")
           
            f2.write(ligne)
           
            num += 1



