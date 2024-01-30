# ctrl+k, ctrl+u/c to un/comment et 
# Exo1
# inverse = []

# def inverser_chaine(chaine):
#     for x in chaine:
#         inverse.insert(0, x)
#     return ''.join(inverse)
# print(inverser_chaine("Bonjour"))


# Exo2
# occurrences = {}
# def compter_lettres(chaine):
#     for lettre in chaine:
#         if lettre in occurrences:
#             occurrences[lettre] += 1
#         else:
#             occurrences[lettre] = 1
#     return occurrences
# print(compter_lettres("hello"))

# Exo3
# chaine_palindrome = "radar"
# chaine_not_palindrome = "python "
# def est_palindrome(chaine):
#     chaine = chaine.lower().replace(' ','')
#     return chaine == chaine[::-1]
# print(est_palindrome(chaine_palindrome))
# print(est_palindrome(chaine_not_palindrome))

# Exo4
# def remplacer_espaces(chaine):
#     chaine = chaine.replace(' ','-')
#     return chaine
# print(remplacer_espaces("Bonjour le monde"))

# Exo5
# def trouver_le_plus_long_mot(phrase):
#     mots = phrase.split()
#     plus_long_mot = ""
#     for mot in mots:
#         if len(mot) > len(plus_long_mot):
#             plus_long_mot = mot
#     return plus_long_mot
# print(trouver_le_plus_long_mot("Le python est un excellent langage de programmation"))

# Exo6
# import re
# def detecter_dates(chaine):
#     pattern = r'\b\d{2}/\d{2}/\d{4}\b'
#     matches = re.findall(pattern, chaine)
#     return matches
# print(detecter_dates("Les dates importantes sont 12/05/2022 et 23/11/2023."))

# Exo7

# print(inverser_liste([1, 2, 3, 4, 5])) # Affiche [5, 4, 3, 2, 1]
