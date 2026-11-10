import random

# Titre de l'application
print("==========================")
print("Bienvenue chez Air Canada!")
print("==========================")

# Envoyer les options de statut à l'utilisateur 

print("\nVeuillez sélectionner votre statut:")
print("1. Client")
print("2. Employé")

# Choix entre client ou employé

statut = input("\nChoix (1/2) : ")

# Dictionnaire des salaires par rôle et ancienneté (en années)

salaires = {
    "directeur": {0: 100000, 5: 120000, 10: 150000},
    "pilote": {0: 80000, 5: 100000, 10: 130000},
    "hotesse de l'air": {0: 35000, 5: 45000, 10: 60000},
    "steward": {0: 35000, 5: 45000, 10: 60000},
    "ramp agent": {0: 30000, 5: 35000, 10: 40000},
    "bagagiste": {0: 25000, 5: 30000, 10: 35000}
}

# Si l'utilisateur est un employé, demander pour son mot de passe

if statut == "2":
    mot_de_passe = input("\nVeuillez entrer votre mot de passe : ")

# Si le mot de passe est correct, afficher le menu des salaires

    if mot_de_passe == "air_canada":
        print("Mot de passe correct. Bienvenue, employé!")
        option_employer = input("\nVeuillez choisir une option :\n1. Voir les salaires \n2. Voir les clients\n\nChoix: ")

# Si l'employer choisi de voir les salaires, afficher le menu des salaires

        if option_employer == "1":
            print("\nMerci de faire partie de notre équipe! Veuillez indiquer votre rôle:")
            print("1. Directeur\n2. Pilote\n3. Hôtesse de l'air\n4. Steward\n5. Ramp Agent\n6. Bagagiste")

# Demander à l'employé de choisir son rôle et une dictionnaire d'emplois

            role_choisi = input("Choisissez votre rôle (1-6) : ")
            roles = ["directeur", "pilote", "hotesse de l'air", "steward", "ramp agent", "bagagiste"]
            role = roles[int(role_choisi) - 1]

# Demander à l'employé d'indiquer son ancienneté pour son rôle

            anciennete = int(input(f"Combien d'années avez-vous travaillé en tant que {role}? : "))
            if anciennete >= 10:
                salaire = salaires[role][10]
            elif anciennete >= 5:
                salaire = salaires[role][5]
            else:
                salaire = salaires[role][0]

# Afficher le salaire de l'employé avec son rôle et ancienneté

            print(f"\nVotre salaire annuel en tant que {role.capitalize()} avec {anciennete} années d'expérience est de : {salaire} $")
            exit()  

# Si l'employer choisi l'option 2 (voir une liste des clients), afficher une liste de clients existants
        elif option_employer == "2":
            clients = "\n - John Smith \n - Emily Johnson \n - Michael Brown \n - Sarah Davis \n - David Wilson \n - Emma Martinez \n - James Taylor \n - Olivia Anderson \n - Daniel Thomas \n - Sophia Moore \n - Matthew Lee \n - Isabella Harris \n - Andrew Walker \n - Mia Young \n - Joseph Hall \n - Chloe King \n - Christopher Allen \n - Ava Scott \n - Samuel Wright \n - Grace Green \n - Benjamin Adams \n - Lily Baker \n - Anthony Clark \n - Ella Nelson \n - Joshua Rodriguez \n - Zoe Carter \n - Ryan Lewis \n - Charlotte Perez \n - Ethan White \n - Abigail Turner"
            print("\nVoici les noms des clients enregistrer en Air Canada:\n\n ", clients)
        else:
            print("Option invalide. Veuillez réessayer.")

# Si le mot de passe est incorrect, afficher un message d'erreur

    else:
        print("Mot de passe incorrect. Veuillez réessayer.")

# Si l'utilisateur est un client, on continue avec la réservation de vol

elif statut == "1":
    print("\n--------------------------\nBienvenue dans Air Canada!\n--------------------------")
    print("\nNous allons vous aider à calculer votre prix de vol.")
    print("Les prix varient en fonction de l'âge des voyageurs et du pays choisi.")

# Affichage des destinations disponibles

    print("\nVoici les destinations disponibles:\n----------------------------------")
    print("\n1. Japon \n2. Thaïlande \n3. Indonésie \n4. Chine \n5. Inde \n6. Viêt Nam \n7. Corée du Sud \n8. France")
    print("9. Grèce \n10. Italie \n11. Islande \n12. Espagne \n13. Suisse \n14. Norvège \n15. Portugal")
    print("16. Allemagne \n17. États-Unis \n18. Canada \n19. Mexique \n20. Pérou \n21. Brésil \n22. Argentine")
    print("23. Afrique du Sud \n24. Égypte \n25. Maroc \n26. Kenya \n27. Australie \n28. Nouvelle-Zélande")
    print("29. Russie \n30. Turquie.")

# Collecte des informations du client

    client_name = input("\nEntrez le nom de famille pour la réservation: ")
    client_email = input("\nEntrez votre adresse email : ")
    choixpays = input("\nVeuillez indiquer votre destination de voyage : ").lower()

# Dictionnaire des prix par âge

    prix_vol = {
        "japon": [400, 500, 700, 600],
        "thaïlande": [350, 450, 650, 550],
        "indonésie": [330, 420, 620, 530],
        "chine": [370, 470, 670, 570],
        "inde": [320, 420, 600, 500],
        "viêt nam": [340, 440, 630, 530],
        "corée du sud": [380, 480, 680, 580],
        "france": [250, 350, 550, 450],
        "grèce": [230, 330, 520, 420],
        "italie": [240, 340, 540, 440],
        "islande": [280, 380, 580, 480],
        "espagne": [260, 360, 560, 460],
        "suisse": [270, 370, 570, 470],
        "norvège": [290, 390, 590, 490],
        "portugal": [240, 340, 540, 440],
        "allemagne": [250, 350, 550, 450],
        "états-unis": [300, 400, 600, 500],
        "canada": [200, 300, 500, 400],
        "mexique": [220, 320, 520, 420],
        "pérou": [330, 430, 630, 530],
        "brésil": [340, 440, 640, 540],
        "argentine": [350, 450, 650, 550],
        "afrique du sud": [370, 470, 670, 570],
        "égypte": [280, 380, 580, 480],
        "maroc": [260, 360, 560, 460],
        "kenya": [290, 390, 590, 490],
        "australie": [400, 500, 700, 600],
        "nouvelle-zélande": [420, 520, 720, 620],
        "russie": [310, 410, 610, 510],
        "turquie": [270, 370, 570, 470]
    }

# Demande à l'utilisateur d'indiquer le nombre de voyageurs qu'il veut enregistrer

    nombre_de_voyageurs = int(input("\nVeuillez indiquer le nombre de voyageurs : "))

# Calcul du prix total et collecte des prénoms

    prix_total = 0
    voyageurs = []

# Boucle pour collecter les prénoms, nom et l'âge de chaque voyageur

    for i in range(nombre_de_voyageurs):
        prenom = input(f"\nEntrez le prénom du voyageur {i + 1} : ")
        nom = input(f"Entrez le nom du voyageur {i + 1} : ")
        age = int(input(f"Veuillez indiquer l'âge du voyageur {i + 1} : "))

# Détermination du prix en fonction de l'âge

        if age <= 12:
            prix = prix_vol[choixpays][0]
        elif 13 <= age <= 18:
            prix = prix_vol[choixpays][1]
        elif 19 <= age <= 64:
            prix = prix_vol[choixpays][2]
        else:
            prix = prix_vol[choixpays][3]

# Afficher le prix pour le voyageur, ajout du prix au prix total et ajout du voyageur à la liste

        print(f"Le prix pour {prenom} {nom} est : {prix} $")
        prix_total += prix

        voyageurs.append({"prenom": prenom, "nom": nom, "age": age, "prix": prix})

# Lister les repas et boissons avec une prix spécifique, ou l'option de rien acheter

    repas_disponibles = {"1. Poulet 15.00$": 15.00, "2. Boeuf 20.00$": 20.00, "3. Végétarien 12.00$": 12.00, "4. Rien 0.00$": 0.00}
    boissons_disponibles = {"1. Jus d'orange 3.00$": 3.00, "2. Jus de pomme 3.00$": 3.00, "3. Café 2.50$": 2.50, "4. Rien 0.00$": 0.00}

    for i in range(nombre_de_voyageurs):
        print(f"\n\n\n\nOptions de repas pour {voyageurs[i]['prenom']} {voyageurs[i]['nom']} :\n----------------------------------")
        for repas in repas_disponibles:
            print(repas)


# Demander à l'utilisateur s'il souhaite acheter des repas et des boissons pour chaque voyageur

        choix_repas = int(input(f"Choisissez le numéro du repas pour {voyageurs[i]['prenom']} : "))
        prix_total += list(repas_disponibles.values())[choix_repas - 1]
        voyageurs[i]['repas'] = list(repas_disponibles.keys())[choix_repas - 1]

        print(f"\n\n\nOptions de boissons pour {voyageurs[i]['prenom']} {voyageurs[i]['nom']} :\n----------------------------------")
        for boisson in boissons_disponibles:
            print(boisson)

        choix_boisson = int(input(f"Choisissez le numéro de la boisson pour {voyageurs[i]['prenom']} : "))
        prix_total += list(boissons_disponibles.values())[choix_boisson - 1]
        voyageurs[i]['boisson'] = list(boissons_disponibles.keys())[choix_boisson - 1]

# Variables d'informations aléatoires pour le vol

    numero_vol = random.randint(1000, 9999)
    siege = random.randint(1, 50)
    heure_depart = f"{random.randint(5, 23)}:{random.randint(0, 59):02}"
    heure_arrivee = f"{(int(heure_depart.split(':')[0]) + random.randint(5, 12)) % 24}:{random.randint(0, 59):02}"

# Affichage du reçu final pour le vol

    print("\n\n-------- Reçu Air Canada --------")
    print(f"\nClient : {client_name}")
    print(f"Email : {client_email}")
    print(f"Destination : {choixpays.capitalize()}")
    print(f"Numéro de vol : {numero_vol}")
    print(f"Numéro de siège : {siege}")
    print(f"Heure de départ : {heure_depart}")
    print(f"Heure d'arrivée : {heure_arrivee}")

# Affichage de la liste des voyageurs avec leurs informations

    print("\n\n-------- Liste des voyageurs --------")
    for i, voyageur in enumerate(voyageurs, start=1):
        print(f"\n\n\nVoyageur {i} :\n----------")
        print(f"Prénom : {voyageur['prenom']}")
        print(f"Nom : {voyageur['nom']}")
        print(f"Âge : {voyageur['age']}")
        print(f"Prix : {voyageur['prix']}")
        print(f"Repas : {voyageur['repas']}")
        print(f"Boisson : {voyageur['boisson']}\n")

    print(f"\nPrix total à payer : {prix_total:.2f} $")

# Remerciment et confirmation de la réservation avec des règles de sécurité

    print("\n\n\n\n\n------------------Merci pour choisir Air Canada------------------")
    print("\n\n\n\n\nVoici les informations pertinentes et importantes pour votre vol:")
    print("\n\n1. Ceinture de sécurité : Attachez-la pendant le décollage, l'atterrissage et en cas de turbulences. \n\n2. Consignes de sécurité : Écoutez l'équipage et lisez la carte de sécurité. \n\n3. Masques à oxygène : Mettez le vôtre en cas de dépressurisation. \n\n4. Gilets de sauvetage : Utilisez-le en cas d'urgence sur l'eau.")

# Si le statut de l'utilisateur n'est ni employé ni client, afficher un message d'erreur

else:
    print("\nStatut invalide. Veuillez redémarrer le programme.")