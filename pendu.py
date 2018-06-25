import random

#creation d'une liste de mot ainsi que la selection aleatoire
liste_mots = ["voiture", "chat","jardin","cours","barriere"]
mot = random.choice(liste_mots)

#demande de saisie de caractere UN seul
lettre_saisie = input("veuillez saisir un caractere:")
print(lettre_saisie)
while len(lettre_saisie) >1:
  print("UN seul caracetere,recommencer") 
  lettre_saisie = input("veuillez saisir un caractere:")
else:
  print("la lettre saisie est "+ lettre_saisie)

# dissimuler le mot
mot_cache = ""
for lettre in mot:
  mot_cache += "*"
print(mot_cache)

# verifier si lettre_saisie existe dans mot
for lettre in mot 
  if lettre_saisie == lettre
    mot_cache += lettre_saisie
  else:
    mot_cache += "*"
