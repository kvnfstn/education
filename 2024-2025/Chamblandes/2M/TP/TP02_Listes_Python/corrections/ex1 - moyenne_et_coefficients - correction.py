############ CONSTANTES - NE PAS MODIFIER ############
matieres = ["Maths", "Français", "Anglais", "Italien", "Chimie", "Physique", "Sport", "Informatique"]

notes = [5.5, 5, 4, 3.5, 3.75, 2, 5.5, 6]
coefficients = [8, 5, 3, 3, 5, 7, 2, 5]

moyenne = None
############ ECRIRE LE CODE CI-DESSOUS ############


# Solution 1
nombre_matieres = 8
somme_coefficients = 0
somme_des_notes_avec_coefficients = 0


for i in range(nombre_matieres): # on a besoin de faire 2 choses:
    # 1. mettre à jour la somme des coefficients en les sommant
    somme_coefficients = somme_coefficients + coefficients[i]
    
    # 2. actualiser la somme des notes fois leur coefficient associé
    somme_des_notes_avec_coefficients = somme_des_notes_avec_coefficients + notes[i]*coefficients[i]

moyenne = somme_des_notes_avec_coefficients/somme_coefficients


# Solution 2
somme_coefficients = sum(coefficients)

somme_des_notes_avec_coefficients = 0

for note, coeff in zip(notes, coefficients):
    somme_des_notes_avec_coefficients = somme_des_notes_avec_coefficients + note*coeff 
    
moyenne = somme_des_notes_avec_coefficients/somme_coefficients


############ ECRIRE LE CODE CI-DESSUS ############


print("La moyenne de l'élève est de :", moyenne) # devrait afficher 4.348684210526316


if moyenne > 6 or moyenne < 1:
    print("Je pense qu'il y a une erreur dans vos calculs...")