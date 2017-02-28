Analyseur de sentiment dans un texte
par Antoine De Laere

Fonctionnement:
Charge les exemples des fichiers 'negative' et 'positive' pour créer le classifier.
Le chargement n'est fait qu'une seule fois, et ne sera pas répété après chaque utilisation des fonctions ci dessous.

fonction principale:

analyse(String):
Retourne un résultat selon si le texte est à connotation positive ou négative et enregistre le texte dans le fichier respectif


apprentissage(String):

Retourne également le résultat mais demande confirmation à l'utilisateur pour enregistrer dans le fichier correct.