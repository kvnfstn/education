#################################### Constantes - NE PAS MODIFIER #################################

la_classe_de_2M42 = ["Léon", "Maya", "Noah", "Amina", "Chloé", "Ibou", "Sakura", "Luc", "Sofia", "Elena", "Ethan", "Nia", "Raph", "Lina", "Julien", "Sara", "Hugo", "Aaron", "Yafi"]
en_retenue = [["Zoé", "Max"], ["Anissa", "Juan"], ["Dan"]]
les_ptits_nouveaux = ["Oli", "Flo"]

######################## Variables à rendre - NE PAS MODIFIER CETTE SECTION #######################

nb_eleves = None
la_classe_de_2M42_bis = la_classe_de_2M42.copy()
la_classe_de_2M42_sans_Sara = la_classe_de_2M42.copy()
en_retenue_bis = en_retenue.copy()
la_classe_de_2M42_avec_les_nouveaux = la_classe_de_2M42.copy()

###################################################################################################
#################################### ECRIRE VOTRE CODE CI-DESSOUS #################################


... 


#################################### ECRIRE VOTRE CODE CI-DESSUS ##################################
###################################################################################################


#################################### Vérification - NE PAS MODIFIER ###############################

print("\n", "Dans la classe 2M42, il y a", nb_eleves, "élèves.")

if la_classe_de_2M42_bis[0] == "Sara" and "Sara" not in la_classe_de_2M42_bis[1:]:
    print("\n", "Sara bien été déplacée tout devant!")
elif la_classe_de_2M42_bis[0] == "Sara" and "Sara" in la_classe_de_2M42_bis[1:]:
    print("\n", "Bunshin no Jutsu, Sara s'est clonée et se trouve maintenant à la fois à la place 0 et", la_classe_de_2M42_bis[1:].index("Sara"))
else:
    print("\n", "Sara n'a pas été déplacée sur le devant de la classe.")

if "Sara" in la_classe_de_2M42_sans_Sara:
    print("\n", "Sara aurait du être envoyée en retenue, mais elle est encore dans la classe...")
else:
    print("\n", "Sara a été exclue du cours!")

if "Sara" in en_retenue_bis[2]:
    print("\n", "Sara est allée s'asseoir a côté de Dan.")
else:
    print("\n", "J'avais demandé à ce que Sara soit assise à la table de Dan !")

if "Oli" in la_classe_de_2M42_avec_les_nouveaux and "Flo" in la_classe_de_2M42_avec_les_nouveaux:
    print("\n", "Je vois que l'intégration des 2 nouveaux s'est bien déroulée!")
else:
    print("\n", "Oli et/ou Flo n'ont pas réussi à arriver jusqu'à leur nouvelle classe...")
    

