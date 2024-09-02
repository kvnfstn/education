#################################### Constantes - NE PAS MODIFIER #################################

scores_solo = [1200, 1500, 800, 2000, 1400, 900, 1700, 1600, 1900, 1000]
scores_razzia_3v3 = [scores_solo[0:3], scores_solo[3:6]] 

######################## Variables à rendre - NE PAS MODIFIER CETTE SECTION #######################

top_players_solo = []
scores_razzia_combines_par_equipe = []
scores_solo_newbie = []

###################################################################################################
#################################### ECRIRE VOTRE CODE CI-DESSOUS #################################


...


#################################### ECRIRE VOTRE CODE CI-DESSUS ##################################
###################################################################################################


#################################### Vérification - NE PAS MODIFIER ###############################

print("Il y a", len(top_players_solo), "top players.")

print("Les scores par équipes sont", scores_razzia_combines_par_equipe, "ce qui fait de l'équipe à la position", 
      scores_razzia_combines_par_equipe.index(max(scores_razzia_combines_par_equipe)), "la gagnante de la partie !")

print("Le nouveau top 3 est situé aux positions", [scores_solo_newbie.index(n) for n in sorted(scores_solo_newbie, reverse=True)[:3]])