def distance_to_toilettes(nombre_marches, hauteur_marche):
    nombre_jours_semaine = 7
    nombre_allers_retours_par_jour = 10
    distance_par_marche = hauteur_marche /100  # Convertir la hauteur en mètres
    distance_par_aller_retour = distance_par_marche * nombre_marches * nombre_allers_retours_par_jour
    distance_par_semaine = distance_par_aller_retour * nombre_jours_semaine

    return distance_par_semaine

# Exemple d'utilisation avec 100 marches de 20 cm
nombre_marches = 102
hauteur_marche = 21 
distance = distance_to_toilettes(nombre_marches, hauteur_marche)

print("Pour", nombre_marches, "marches de", hauteur_marche,"cm" " ""le gardien parcourt", f"{distance:.2f}", "m par semaine.")

