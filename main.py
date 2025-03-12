from module import ajouter_patient,supprimer_patient,liste_patients_par_prioriter,mise_en_forme_liste_patients_par_prioriter,is_number

patients_complet = []

while True:
    print("----- Veuillez Entrez les informations du patient -----")
    nom_patient = input("Entrez le nom du patient : ")

    age_patient = input("Entrez l'age du patient : ")
    while not is_number(age_patient):
        age_patient = input("Veuillez entrez un age valide : ")

    statut_patient = input("Entrez le statut du patient N (Normal) E (Enceinte) : ")
    while statut_patient != "N" and statut_patient != "E":
        statut_patient = input("Veuillez entrez un statut valide N (Normal) E (Enceinte) : ")

    patients_complet = ajouter_patient(nom_patient, age_patient, statut_patient)

    arret = input("Tappez la touche ENTRER pour continuer ou tapez Q pour quitter: ")
    if arret == "Q":
        break

liste_patients_final = liste_patients_par_prioriter(patients_complet)
print(mise_en_forme_liste_patients_par_prioriter(liste_patients_final))

print("----- Simmulation de la prise en charge des patients et Suppression des patients -----")
for patient in patients_complet:
    supprimer_patient(patient[0],patients_complet)

print(mise_en_forme_liste_patients_par_prioriter(patients_complet))

