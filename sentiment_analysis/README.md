Analyseur de sentiment dans un texte
par Antoine De Laere

Fonctionnement:
Charge les exemples des fichiers 'negative' et 'positive' pour cr�er le classifier.
Le chargement n'est fait qu'une seule fois, et ne sera pas r�p�t� apr�s chaque utilisation des fonctions ci dessous.

fonction principale:

analyse(String):
Retourne un r�sultat selon si le texte est � connotation positive ou n�gative et enregistre le texte dans le fichier respectif


apprentissage(String):

Retourne �galement le r�sultat mais demande confirmation � l'utilisateur pour enregistrer dans le fichier correct.