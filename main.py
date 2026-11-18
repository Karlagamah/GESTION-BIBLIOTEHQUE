from controllers import bibliotheque_controller
from models.database import creer_tables, ajouter_livres_par_defaut
from views import menu_view

creer_tables()
ajouter_livres_par_defaut()
choix = -1

while choix != 0:
    choix = menu_view.afficher_menu()

    if choix == 1:
        bibliotheque_controller.ajouter_un_livre()
    elif choix == 2:
        bibliotheque_controller.afficher_les_livres()
    elif choix == 3:
        bibliotheque_controller.rechercher_un_livre()
    elif choix == 4:
        bibliotheque_controller.supprimer_un_livre()
    elif choix == 5:
        bibliotheque_controller.ajouter_un_membre()
    elif choix == 6:
        bibliotheque_controller.afficher_les_membres()
    elif choix == 7:
        bibliotheque_controller.emprunter_un_livre()
    elif choix == 8:
        bibliotheque_controller.retourner_un_livre()
    elif choix == 9:
        bibliotheque_controller.afficher_les_emprunts()
    elif choix == 0:
        menu_view.afficher_message("Au revoir !")
    else:
        menu_view.afficher_message("Choix invalide.")