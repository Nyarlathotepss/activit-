from random import randrange
from math import ceil

i = randrange(50) #le chiffre aleatoire de la roulette
print(i)
numeromise = input ("veuillez saisir votre numero")
numeromise = int(numeromise)
sommemise = input ("veuillez saisir votre mise")
sommemise =int(sommemise)
gain = int(0)
banque = int(100)

if i == numeromise: #meme numero ?
  gain = sommemise*3
elif i % 2 == 0 and numeromise % 2 == 0:
  gain = sommemise*1.5 #meme couloeur noir et donc pair ?
elif i % 2 != 0 and numeromise % 2 != 0:
  gain = sommemise*1.5 #meme couleur rouge et donc impair ?
else :
  gain = 0

banque = banque - sommemise + ceil(gain)
print(banque)
