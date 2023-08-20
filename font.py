
list_fruit = ("mangue","pomme","banane","coco")
nom_fichier = input("Entrez le nom du fichier: ")
with open('ahh.txt', "w") as f: 
    for fruit in list_fruit:
        f.write(fruit + "\n")

