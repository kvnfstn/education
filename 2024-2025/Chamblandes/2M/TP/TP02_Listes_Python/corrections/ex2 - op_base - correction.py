######################## Variables à rendre - NE PAS MODIFIER CETTE SECTION #######################

une_liste_incomplete = ["Oh", "Djadja", "Y a", "pas", "moyen"]
une_liste_heterogene = [3, "Dix-sept", "Neuf", "Trente"]
une_liste_avec_trop_de_trucs = ["un petit chocolat", 3.14, "on peut faire plein de trucs chouettes avec la prog", 17, "une string vide", True]

###################################################################################################
#################################### ECRIRE VOTRE CODE CI-DESSOUS #################################


une_liste_incomplete.append("Djadja") 

une_liste_heterogene[1] = 17
une_liste_heterogene[2] = 9
une_liste_heterogene[3] = 30

une_liste_avec_trop_de_trucs.remove(3.14)
une_liste_avec_trop_de_trucs.remove(17)
une_liste_avec_trop_de_trucs.remove(True)
une_liste_avec_trop_de_trucs.remove(17)


#################################### ECRIRE VOTRE CODE CI-DESSUS ##################################
###################################################################################################


#################################### Vérification - NE PAS MODIFIER ###############################

print(une_liste_incomplete) # devrait afficher ["Oh", "Djadja", "Y a", "pas", "moyen", "Djadja"]
print(une_liste_heterogene) # devrait afficher [3, 17, 9, 30]
print(une_liste_avec_trop_de_trucs) # devrait afficher ["un petit chocolat", "on peut faire plein de trucs chouettes avec la prog", "une string vide"]