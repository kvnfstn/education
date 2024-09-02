############ CONSTANTES - NE PAS MODIFIER ############
matieres = ["Maths", "Français", "Anglais", "Italien", "Chimie", "Physique", "Sport", "Informatique"]

notes = [5.5, 5, 4, 3.5, 3.75, 2, 5.5, 6]

moyenne = None
############ ECRIRE LE CODE CI-DESSOUS ############

# Solution 1
nombre_notes = len(notes) # ou nombre_matieres = len(matieres)
somme_des_notes = 0

for note in notes:
    somme_des_notes = somme_des_notes + note # pour aller plus loin : `sommes_des_notes += note`
    
moyenne = somme_des_notes/nombre_notes

# Solution 2
nombre_notes = 8
somme_des_notes = 0

for i in range(nombre_notes):
    somme_des_notes = somme_des_notes + notes[i] 

moyenne = somme_des_notes/nombre_notes

# Solution 3
moyenne = sum(notes)/len(notes) 



############ ECRIRE LE CODE CI-DESSUS ############


print("La moyenne de l'élève est de :", moyenne)


if moyenne > 6 or moyenne < 1:
    print("Je pense qu'il y a une erreur dans vos calculs...")