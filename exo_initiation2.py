# Exo1
# import platform
# import socket

# def informations_systeme():
#     # Nom d'hôte
#     nom_hote = socket.gethostname()

#     # Adresse IP
#     adresse_ip = socket.gethostbyname(nom_hote)

#     # Architecture du processeur
#     architecture_processeur = platform.processor()

#     # Version du système d'exploitation
#     version_os = platform.system() + " " + platform.release()

#     # Affichage des informations
#     print(f"Nom d'hôte : {nom_hote}")
#     print(f"Adresse IP : {adresse_ip}")
#     print(f"Architecture du processeur : {architecture_processeur}")
#     print(f"Version du système d'exploitation : {version_os}")

# if __name__ == "__main__":
#     informations_systeme()

# Exo2 Lister fichiers d'un répertoire spécifié
# import os

# def lister_fichiers_et_tailles(dossier):
#     try:
#         # Liste tous les fichiers dans le dossier spécifié
#         fichiers = os.listdir(dossier)

#         # Parcours de chaque fichier
#         for fichier in fichiers:
#             chemin_complet = os.path.join(dossier, fichier)
            
#             # Vérifie si c'est un fichier (et non un sous-dossier)
#             if os.path.isfile(chemin_complet):
#                 # Obtient la taille du fichier en octets
#                 taille = os.path.getsize(chemin_complet)

#                 # Affiche le nom du fichier et sa taille
#                 print(f"{fichier} - Taille: {taille} octets")

#     except FileNotFoundError:
#         print(f"Le dossier '{dossier}' n'existe pas.")
#     except PermissionError:
#         print(f"Permission refusée pour accéder au dossier '{dossier}'.")
#     except Exception as e:
#         print(f"Une erreur s'est produite : {e}")

# # Test de la fonction
# dossier_test = "."  # Remplacez par le chemin de votre dossier spécifié
# lister_fichiers_et_tailles(dossier_test)

# Exo3 Memoire systeme
# import psutil

# def afficher_utilisation_memoire():
#     # Obtient les statistiques d'utilisation de la mémoire
#     memoire = psutil.virtual_memory()

#     print(f"Utilisation de la mémoire du système :")
#     print(f"  Total: {memoire.total} octets")
#     print(f"  Disponible: {memoire.available} octets")
#     print(f"  Utilisé: {memoire.used} octets")
#     print(f"  Pourcentage d'utilisation: {memoire.percent}%")

# if __name__ == "__main__":
#     afficher_utilisation_memoire()

# Exo4 surveille usage CPU
# import psutil
# import time

# def surveiller_utilisation_cpu():
#     try:
#         while True:
#             # Obtient l'utilisation du CPU en pourcentage
#             cpu_percent = psutil.cpu_percent(interval=1)

#             print(f"Utilisation du CPU : {cpu_percent}%")

#             # Attente de 5 secondes
#             time.sleep(5)

#     except KeyboardInterrupt:
#         print("Arrêt de la surveillance.")

# if __name__ == "__main__":
#     surveiller_utilisation_cpu()

# Exo5 check espace DD
import psutil

def verifier_espace_disque():
    try:
        # Obtient les statistiques d'utilisation de l'espace disque principal
        espace_disque = psutil.disk_usage('/')

        print(f"Espace disque principal :")
        print(f"  Total: {espace_disque.total} octets")
        print(f"  Utilisé: {espace_disque.used} octets")
        print(f"  Disponible: {espace_disque.free} octets")
        print(f"  Pourcentage d'utilisation: {espace_disque.percent}%")

    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

if __name__ == "__main__":
    verifier_espace_disque()

