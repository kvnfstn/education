######################## Constantes - NE PAS MODIFIER CETTE SECTION ###############################

mauvaise_raclette = ["Nutella", "Kiwi", "Fromage", "Patates", "Glace vanille"]
mauvaise_crepe = ["oeufs", "lait", "farine", "sucre", "ciment", "plastique", "miel", "citron"]

artistes_1 = ["Billie Eilish", "The Weeknd", "Ninho", "Dinos"] 
artistes_2 = ["Yamê", "Dua Lipa", "Ed Sheeran", "Aya Nakamura"]

######################## Variables à rendre - NE PAS MODIFIER CETTE SECTION #######################

bonne_raclette = []
bonne_crepe = mauvaise_crepe.copy()

artistes_pop = []
artistes_rap = [] 

###################################################################################################
#################################### ECRIRE VOTRE CODE CI-DESSOUS #################################


bonne_raclette = mauvaise_raclette[2:4]
bonne_crepe[4:6] = [] # ou alors: mauvaise_crepe[0:4] + mauvaise_crepe[6:] 

artistes_pop = artistes_1[0:2] + artistes_2[1:3]

artistes_rap = artistes_1[2:4]
artistes_rap.append(artistes_2[0])
artistes_rap.append(artistes_2[3])  
# ou alors: artistes_rap = artistes_1[2:4] + [artistes_2[0]] + [artistes_2[3]]

#################################### ECRIRE VOTRE CODE CI-DESSUS ##################################
###################################################################################################


#################################### Vérification - NE PAS MODIFIER ###############################

if len(bonne_raclette) != 2:
    print("\n", "Je ne veux que 2 ingrédients dans ma raclette mais là j'en ai", len(bonne_raclette))
else:
    if "Fromage" in bonne_raclette and "Patates" in bonne_raclette:
        print("\n", "Une bonne raclette se fait toujours avec ces 2 ingrédients :", ", ".join(bonne_raclette))
    else:
        print("\n", ", ".join(bonne_raclette), ": je crois que ce ne sont pas les bons ingrédients pour une raclette...")


if len(bonne_crepe) != 6:
    print("\n", "Je veux faire mes crêpes avec 6 ingrédients, pas", len(bonne_crepe))
else:
    if "ciment" in bonne_crepe or "plastique" in bonne_crepe:
        print("\n", "Une crêpe avec du ciment ou du plastique, vous êtes sûrs ?")
    else:
        print("\n", ", ".join(bonne_crepe), ": de quoi faire d'excellentes crêpes !")


if sorted(artistes_pop) == ["Billie Eilish", "Dua Lipa", "Ed Sheeran", "The Weeknd"]:
    print("\nLes artistes pop sont prêt·e·s pour les Grammy Awards ! Qui va gagner ?")
else:
    print("\nJ'ai l'impression qu'il y a un·e intrus·e chez les artistes pop...", artistes_pop)

if sorted(artistes_rap) == ["Aya Nakamura", "Dinos", "Ninho", "Yamê"]:
    print("\nLes artistes rap sont prêt·e·s pour les Flammes ! Qui va gagner ?")
else:
    print("\nJ'ai l'impression qu'il y a un·e intrus·e chez les artistes rap...", artistes_rap)
