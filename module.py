nom_patiens = []
ages_patients = []
statut_patients = []
prioriter_patients_Enceinte = []
prioriter_personne_agee_et_normale = []


def ajouter_patient(nom_patient, age_patient, statut_patient):
    nom_patiens.append(nom_patient)
    ages_patients.append(age_patient)
    statut_patients.append(statut_patient)
    print(f"-> Patient {nom_patient} ajouté à la liste")
    return list(zip(nom_patiens, ages_patients, statut_patients))


def supprimer_patient(nom, patients_complet):
    for patient in patients_complet:
        if patient[0] == nom:
            patients_complet.remove(patient)
            print(f"-> Patient {nom} fin de prise en charge, supprimé de la liste")


def liste_patients_par_prioriter(liste):
    # tri des patients par age
    liste.sort(key=lambda x: x[1], reverse=True)
    # tri des patients par statut
    liste.sort(key=lambda x: x[2])

    for patient in liste:
        if patient[2] == "E":
            prioriter_patients_Enceinte.append(patient)
        else:
            prioriter_personne_agee_et_normale.append(patient)

    return prioriter_patients_Enceinte + prioriter_personne_agee_et_normale


def mise_en_forme_liste_patients_par_prioriter(liste):
    print("\n----- la liste des patients par prioriter est : -----")
    for patient in liste:
        print(f"nom : {patient[0]} , age : {patient[1]} , statut : {patient[2]}")


# verifier si l'input est un nombre
def is_number(nbr):
    try:
        int(nbr)
        return True
    except ValueError:
        return False
