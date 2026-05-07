
 
#ppattie fait par verdi
def calculatrice():
    print("=== Calculatrice Simple ===")
    print("Opérations : + | - | * | /")
    print("Tapez 'quitter' pour arrêter\n")
#partie de leslie
while True:
        entree = input("Entrez un calcul (ex: 5 + 3) : ")

        if entree.lower() == "quitter":
            print("Au revoir !")
            breaks
        try:
            # Séparer les éléments
            parties = entree.split()
            nombre1 = float(parties[0])
            operateur = parties[1]
            nombre2 = float(parties[2])

            # Calculer
            if operateur == "+":
                resultat = nombre1 + nombre2
            elif operateur == "-":
                resultat = nombre1 - nombre2
            elif operateur == "*":
                resultat = nombre1 * nombre2
            elif operateur == "/":
                if nombre2 == 0:
                    print("Erreur : division par zéro !\n")
                    continue
                resultat = nombre1 / nombre2
            else:
                print("Opérateur inconnu. Utilisez + - * /\n")
                continue

            print(f"Résultat : {nombre1} {operateur} {nombre2} = {resultat}\n")

        except (IndexError, ValueError):
            print("Format invalide. Exemple correct : 5 + 3\n")

# Lancer la calculatrice
calculatrice()

